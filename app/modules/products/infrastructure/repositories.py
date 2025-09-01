# Իմպորտներ
from sqlalchemy.orm import Session
from sqlalchemy import select

# Իմպորտում ենք մեր SQLAlchemy մոդելը և Pydantic սխեմաները
from ..domain.models import Product
from ..domain.schemas import ProductCreate


# Տվյալների բազայի հետ աշխատելու համար նախատեսված կլաս
# Այս կլասի միջոցով մենք կկատարենք բոլոր հարցումները
class ProductRepository:
    # Կլասը ընդունում է տվյալների բազայի սեսիա (session) որպես կախվածություն
    def __init__(self, db: Session):
        self.db = db

    # Ստեղծել նոր ապրանք
    def create_product(self, product_data: ProductCreate) -> Product:
        # Ստեղծում ենք Product օբյեկտը՝ հիմնված Pydantic սխեմայի տվյալների վրա
        new_product = Product(**product_data.model_dump())
        # Ավելացնում ենք օբյեկտը սեսիային
        self.db.add(new_product)
        # Պահպանում ենք փոփոխությունները տվյալների բազայում
        self.db.commit()
        # Թարմացնում ենք օբյեկտը՝ ստանալով տվյալների բազայի կողմից ստեղծված ID-ն
        self.db.refresh(new_product)
        return new_product

    # Ստանալ բոլոր ապրանքները
    def get_all_products(self) -> list[Product]:
        # Կատարում ենք հարցում տվյալների բազային բոլոր ապրանքները ստանալու համար
        products = self.db.scalars(select(Product)).all()
        return products

    # Ստանալ ապրանքը ըստ ID-ի
    def get_product_by_id(self, product_id: int) -> Product | None:
        # Կատարում ենք հարցում՝ ֆիլտրելով ըստ ID-ի
        product = self.db.scalars(select(Product).filter_by(id=product_id)).one_or_none()
        return product