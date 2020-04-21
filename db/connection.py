from pymongo import MongoClient
from pprint import pprint

def printServerStatus():
    client = MongoClient("mongodb+srv://develop:develop@watchful-owl-cluster-pyzs6.mongodb.net/test?retryWrites=true&w=majority")
    db=client.watchfulowl
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)

# Devuelve una conexión al cluster de la base de datos
def GetDbClient():
    user = "develop"
    password = "develop"
    client = MongoClient("mongodb+srv://{}:{}@watchful-owl-cluster-pyzs6.mongodb.net/test?retryWrites=true&w=majority".format(user,password))
    return client

def Testing():
    user = "develop"
    password = "develop"
    print("client?")
    client = MongoClient("mongodb+srv://{}:{}@watchful-owl-cluster-pyzs6.mongodb.net/test?retryWrites=true&w=majority".format(user,password))
    print("client:", client)
    db = client.watchfulowl
    result=db.persons.find_one({"email": "juancsr@protonmail.com"})
    print("db: ", db)
    return result
