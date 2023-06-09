from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    tags=["users"],  # el tag sirve para separar las apis en la documentacion
)


# entidad usuario, none means that is optional
class User(BaseModel):
    id: int
    name: str
    sur_name: str
    url: str
    age: int


users_list = [
    User(id=1, name="Jhon", sur_name="Meza", url="jhon.com", age=21),
    User(id=2, name="asda", sur_name="Meza", url="jhon.com", age=21),
]
# Inicia el server: uvicorn users:app --reload


@router.get("/users")
async def users():
    return users_list


# path
@router.get("/user/{id_user}")
async def user_by_id(id_user: int):
    search_user(id_user)


# query
@router.get("/user/")
async def user_by_id(id_user: int):
    search_user(id_user)


# add new user


@router.post("/user/", response_model=User, status_code=201)
async def create_user(new_user: User):
    if type(search_user(new_user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exists")

    users_list.append(new_user)
    return {"message": "User added"}


# update user
@router.put("/user/")
async def update_user(new_user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == new_user.id:
            users_list[index] = new_user
            return {"message": "User updeted"}

    return {"message": "User not found"}


# delete user


@router.delete("/user/{id_user}")
async def delete_user(id_user: int):
    for index, saved_user in enumerate(users_list):
        print(saved_user)
        if saved_user.id == id_user:
            del users_list[index]
            return {"message": "User deleted"}

    return {"message": "User not found"}


# function for searh users
def search_user(id_user: int):
    users_found = filter(lambda user: user.id == id_user, users_list)
    try:
        return list(users_found)[0]
    except:
        return {"message": "User not found "}
