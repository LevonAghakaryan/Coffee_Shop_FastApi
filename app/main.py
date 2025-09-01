# Իմպորտներ
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
# Մոդուլների router-ների ներմուծում
from .modules.orders.presentation.router import router as orders_router
from .modules.products.presentation.router import router as products_router
# from .modules.users.presentation.router import router as users_router

app = FastAPI(title="Coffee Shop API")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")
templates = Jinja2Templates(directory="templates")


# UI-ի համար պարզ endpoint-ներ
@app.get("/", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Մեր Մենյուն"})

@app.get("/products/all_products", include_in_schema=False)
async def products_page(request: Request):
    return templates.TemplateResponse("products/products.html", {"request": request, "title": "Մեր Մենյուն"})

@app.get("/products/create_product", include_in_schema=False)
async def create_product_page(request: Request):
    return templates.TemplateResponse("products/create_product.html", {"request": request, "title": "Ավելացնել Ապրանք"})


# API Router-ների միացում
app.include_router(orders_router)
app.include_router(products_router)
# app.include_router(users_router)