from db.connection import GetDbClient, printServerStatus, Testing
from utils.utils import logger

# Obtiene un usuario a partir de su email
def getUserByEmail(username, password):
    user = None
    try:
        client = GetDbClient()
        db = client.watchfulowl
        user = db.persons.find_one({
            "$or": [{"email": username}, {"user_info.username": username}],
            "user_info.password": password
        })
    except:
        logger("error getting the data", "getUserByEmail")
    
    return user


def defCreateUser():
    return "yei"
