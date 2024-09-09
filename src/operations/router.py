from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select

from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from src.operations.models import Operation
from src.operations.schemas import OperationCreate, DefaultQueryResponse

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_type:str, session: AsyncSession = Depends(get_async_session)) -> DefaultQueryResponse:
    try:
        query = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(query)
        return {
            "status":"success", 
            "data": result.scalars().all(), 
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status":"error", 
            "data": None, 
            "details": None
        })


@router.post("/")
async def add_specific_operations(new_operation:OperationCreate, session: AsyncSession = Depends(get_async_session)) -> DefaultQueryResponse:
    try: 
        stmt = insert(Operation).values(**new_operation.model_dump())
        await session.execute(stmt) #ОПЕРАЦИЯ
        await session.commit() #ИСПОЛНЯЕТ ВСЕ ОПЕРАЦИИ ВЫШЕ
        return {
            "status": "success",
            "data": None,
            "details": None
        } 
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status":"error",
            "data": None, 
            "details": None
        }) 


