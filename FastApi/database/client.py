
# Módulo conexión MongoDB: pip install pymongo
# Conexión: mongodb://localhost

from pymongo import MongoClient

# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
#db_client = MongoClient().local



# Base de datos remota MongoDB Atlas (https://mongodb.com)
db_client = MongoClient(
    "mongodb+srv://jhonmeza:mezajhon@cluster0.m5roivi.mongodb.net/").test

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/
