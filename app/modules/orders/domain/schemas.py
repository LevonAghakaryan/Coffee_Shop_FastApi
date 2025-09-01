from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    customer_name: str
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True # Թույլ է տալիս ուղիղ կոնվերտացնել SQLAlchemy մոդելից