import datetime

from flask import Flask, request, make_response, session
from controllers.person import getUserByEmail
from utils.utils import standarResponse
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

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
        user = getUserByEmail(username, password)
        if user is None:
            return standarResponse(error="User not found")
        user["_id"] = str(user["_id"])
        return standarResponse(user)

# Endpoint para registrar nuevos usuarios
@app.route('/sign-up', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        request_json = request_json.get_json(force=True)
        print(request_json)
    return standarResponse({"data": "user created"})

# Inicio de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
