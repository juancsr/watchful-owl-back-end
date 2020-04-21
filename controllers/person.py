from db.connection import getDbConnection

# Obtiene un usuario a partir de su email
def getUserByEmail(email):
    user = None
    try:
        db = getDbConection()
        user = db.person.find_one({'user_info.email': email})
    except exception:
        logger(String(exception), "getUserByEmail")
    finally:
        return user

# Función para imprimir de una forma genérica los errores de ejecución
def logger(messsage, function="<>"):
    print("Error in: {} => {}".format(function, message))

def defCreateUser():
    return "yei"
