import datetime

#  Este método se encarga de estándarizar todas las respuestas del API, para que tengan siempre la misma estructura
def standarResponse(data={}, error=None):
    response = {
        'date': datetime.datetime.now(),
        'data': data
    }

    if error is not None:
        del response['data']
        response['error'] = error

    return response
