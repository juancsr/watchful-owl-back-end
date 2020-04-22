import datetime
import utils.utils as utils
from controllers import person, aylientextnalysis
from flask_cors import CORS
from flask import Flask, request, make_response, session

app = Flask(__name__)
CORS(app)

# Ruta de prueba
@app.route('/test')
def test():
    return {"message": "is working"}

# Endpoint para logeo de usuari, recibe un json con el atributo email y verifica que el usuario exista
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        username = request_json['user']
        password = request_json['password']
        print(username, password)
        user = person.getUserByEmail(username, password)
        if user is None:
            return utils.standarResponse(error="User not found")
        user["_id"] = str(user["_id"])
        return utils.standarResponse(user)

# Endpoint para registrar nuevos usuarios
@app.route('/sign-up', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        request_json = request_json.get_json(force=True)
        print(request_json)
    return utils.standarResponse({"data": "user created"})

@app.route('/text-classification', methods=['POST'])
def testAylienApi():
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        url = request_json['url']
        result = aylientextnalysis.performsFullAnalysis(url)
        if not result:
            return utils.standarResponse(error="Error with URL")
    return utils.standarResponse(result)

# Inicio de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
