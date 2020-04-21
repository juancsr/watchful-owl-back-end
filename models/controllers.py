from db import getDbConection

def getUserByEmail(email):
    user = None
    try:
        db = getDbConection()
        user = db.person.find_one({'user_info.email': email})
    except exception:
        logger("getUserByEmail", exception)
    finally:
        return user

# Función para imprimir de una forma genérica los errores de ejecución
def logger(function="<>", message):
    print("Error in: {} => {}".format(function, message))

def defCreateUser():
    return "yei"
