from fastapi import APIRouter

# En el caso que yo le indico un prefijo no tengo que ponerlas en las rutas
router = APIRouter(
    prefix="/products",
    tags=["products"], #el tag sirve para separar las apis en la documentacion
    responses={404: {"message": "Product not found"}},
)

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]
