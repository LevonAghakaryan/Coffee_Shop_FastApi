from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Integer, Float
from app.core.database import Base



class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str] = mapped_column(Text)

    price: Mapped[float] = mapped_column(Float, nullable=False)

    img_url: Mapped[str] = mapped_column(String(255), nullable=True)

