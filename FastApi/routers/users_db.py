from fastapi import APIRouter, HTTPException, status
from ..database.models.user import User
from ..database.client import db_client
from ..database.schemas.user import user_schema, users_schema
from bson import ObjectId


router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],  # el tag sirve para separar las apis en la documentacion
    responses={status.HTTP_404_NOT_FOUND: {"message": "user not found"}},
)


# Inicia el server: uvicorn users:app --reload


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())


# path
@router.get("/{id_user}")
async def user_by_id(id_user: str):
    return search_user("_id", ObjectId(id_user))


# query
@router.get("/userbyID/")
async def user_by_id(id_user: str):
    return search_user("_id", ObjectId(id_user))


# add new user


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: User):
    if type(search_user("email", new_user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exists"
        )

    user_dict = dict(new_user)
    del user_dict["id"]
    id = db_client.users.insert_one(
        user_dict
    ).inserted_id  # aqui creo el nombre de mi coleccion

    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)


# update user
@router.put("/", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(new_user: User):
    try:
        
        user_dict = dict(new_user)
        del user_dict["id"]

        db_client.users.find_one_and_replace({"_id": ObjectId(new_user.id)}, user_dict)
    except:
         raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED, detail="User can be edited"
        )
    
    return search_user("_id",ObjectId(new_user.id))


# delete user


@router.delete("/{id_user}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id_user: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id_user)})

    if not found:
        return {"message": "User not found"}


# function for searh users
def search_user(field: str, key: any):
    try:
        user = user_schema(db_client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"message": "User not found "}
