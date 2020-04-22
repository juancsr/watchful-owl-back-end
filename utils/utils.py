import datetime


"""
Se encarga de estándarizar todas las respuestas del API, para que tengan siempre la misma estructura

:param data: data del response
:param function: error del response, por defecto None
:return: un diccionario para responder en formato json
"""
def standarResponse(data={}, error=None):
    response = {
        'date': datetime.datetime.now(),
        'data': data
    }

    if error is not None:
        del response['data']
        response['error'] = error

    return response

"""
Función para imprimir de una forma genérica los errores de ejecución

:param message: mensaje de error
:param function: función donde ocurrio el error, por defecto es '<>'
"""
def logger(message, function="<>"):
    print("Error in: {} => {}".format(function, message))
