from datetime import datetime
from typing import List
from pydantic import BaseModel


class OperationCreate(BaseModel):
    id:int
    quantity:str
    penis:str
    figi:str
    instrument_type:str
    date:datetime
    type:str

class OperationSchema(BaseModel):
    id: int
    quantity: str 
    penis:str
    figi:str
    instrument_type:str
    date: datetime
    type:str

class DefaultQueryResponse(BaseModel):
     status:str
     data:List[OperationSchema]
     details: str | None