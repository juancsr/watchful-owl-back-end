import datetime

from flask import Flask, request, make_response, session
from controllers.person import getUserByEmail
from utils.utils import standarResponse
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

@app.route('/test')
def test():
    return {"message": "is working"}

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        email = request_json['email']
        print("email: {}".format(email))
        user = getUserByEmail(email)
        if user is None:
            return standarResponse(error="User not found")
        return standarResponse(user)

# Inicio de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
