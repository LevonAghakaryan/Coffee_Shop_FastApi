# Իմպորտներ
from fastapi import HTTPException, status

# Իմպորտում ենք մեր repositories և schemas
from ..infrastructure.repositories import ProductRepository
from ..domain.schemas import Product, ProductCreate


# Բիզնես տրամաբանության կլաս
class ProductService:
    # Կլասը ընդունում է repository որպես կախվածություն
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    # Ստեղծել նոր ապրանք
    def create_product(self, product_data: ProductCreate) -> Product:
        # Ստուգում, թե արդյոք արդեն գոյություն ունի նույն անունով ապրանք
        existing_product = self.repository.get_product_by_id(product_data.id)
        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product with this name already exists."
            )

        # Օգտագործում ենք repository-ն՝ ապրանքը տվյալների բազայում պահպանելու համար
        return self.repository.create_product(product_data)

    # Ստանալ բոլոր ապրանքները
    def get_all_products(self) -> list[Product]:
        return self.repository.get_all_products()

    # Ստանալ ապրանքը ըստ ID-ի
    def get_product_by_id(self, product_id: int) -> Product:
        product = self.repository.get_product_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found."
            )
        return product