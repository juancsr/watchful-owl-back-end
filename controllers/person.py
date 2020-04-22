from db.connection import GetDbClient, printServerStatus, Testing
import utils.utils as utils

"""
Obtiene un usuario a partir de su username/email y contraseña, la búsqueda la realiza con el email o el username de la persona

:param username: es el nombre de usuario o el email de la persona
:password: contraseña
:return: un diccionario si se encontró a la persona, de otra forma devuelve un None
"""
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
        utils.logger("error getting the data", "getUserByEmail")
    
    return user


def defCreateUser():
    return "yei"
