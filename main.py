from fastapi import FastAPI
from FastApi.routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Concepto de routers

# app.include_router(products.router)
# app.include_router(users.router)
app.include_router(jwt_auth_users.router)
# app.include_router(basic_auth_users.router)
#app.include_router(users_db.router)
#app.mount("/static", StaticFiles(directory="static"), name="static_image")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}


# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc


# Inicia el server: uvicorn main:app --reload
#mongodb+srv://jhonmeza:mezajhon@cluster0.m5roivi.mongodb.net/