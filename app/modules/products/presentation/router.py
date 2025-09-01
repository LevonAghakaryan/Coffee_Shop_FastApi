# Իմպորտներ
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# Մեր կողմից սահմանված ֆայլերի իմպորտ
from app.core.database import get_db
from ..domain.schemas import ProductCreate, Product
from ..application.services import ProductService
from ..infrastructure.repositories import ProductRepository


# APIRouter-ի օբյեկտի ստեղծում
router = APIRouter(prefix="/products", tags=["products"])


# Կախվածությունների (dependencies) ստեղծումը
# Այս մեթոդը կապահովի, որ յուրաքանչյուր հարցման համար ստեղծվի մեկ ProductService
def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    repository = ProductRepository(db)
    return ProductService(repository)


# Endpoint՝ բոլոր ապրանքները ստանալու համար
@router.get("/AllProducts", response_model=List[Product])
def get_all_products(
    service: ProductService = Depends(get_product_service)
):
    """
    Ստանալ բոլոր ապրանքները մենյուից:
    """
    return service.get_all_products()


# Endpoint՝ նոր ապրանք ավելացնելու համար
@router.post("/CreateProduct", response_model=Product, status_code=201)
def create_product(
    product_data: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    """
    Ստեղծել նոր ապրանք:
    """
    return service.create_product(product_data)