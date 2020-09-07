from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {'ajas': {'age': 21, 'gender': 'male'},
         'ali': {'age': 22, 'gender': 'male'}}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, '/hello-world/<string:name>')
if __name__ == "__main__":
    app.run(debug=True)
