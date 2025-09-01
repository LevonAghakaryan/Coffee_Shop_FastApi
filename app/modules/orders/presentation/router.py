from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from ..application.services import OrderService
from ..domain import schemas

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# Dependency injection-ի միջոցով ստանում ենք service-ը
def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)

@router.post("/", response_model=schemas.OrderRead)
def create_order(
    order: schemas.OrderCreate,
    service: OrderService = Depends(get_order_service)
):
    try:
        return service.place_new_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))