from pymongo import MongoClient
from pprint import pprint

def printServerStatus():
    client = MongoClient("mongodb+srv://develop:develop@watchful-owl-cluster-pyzs6.mongodb.net/test?retryWrites=true&w=majority")
    db=client.admin
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)

# Devuelve una conexión al cluster de la base de datos
def getDbConnection():
    user = "develop"
    password = "develop"
    client = MongoClient("mongodb+srv://{}:{}@watchful-owl-cluster-pyzs6.mongodb.net/test?retryWrites=true&w=majority".format(user,password))
    db = client.watchfulowl
    return db
