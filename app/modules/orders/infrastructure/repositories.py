from sqlalchemy.orm import Session
from ..domain import models, schemas

class OrderRepository:
    def create_order(self, db: Session, order: schemas.OrderCreate) -> models.Order:
        db_order = models.Order(
            customer_name=order.customer_name,
            total_price=order.total_price
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

    def get_order(self, db: Session, order_id: int) -> models.Order | None:
        return db.query(models.Order).filter(models.Order.id == order_id).first()