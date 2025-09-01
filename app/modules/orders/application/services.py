from sqlalchemy.orm import Session
from ..domain import schemas
from ..infrastructure.repositories import OrderRepository

class OrderService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = OrderRepository()

    def place_new_order(self, order: schemas.OrderCreate):
        # Այստեղ կարող է լինել բարդ տրամաբանություն՝
        # օրինակ, զեղչի հաշվարկ, ստուգումներ և այլն։
        if order.total_price <= 0:
            raise ValueError("Price must be positive")
        return self.repository.create_order(db=self.db, order=order)