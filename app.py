from routes.plates import Plate, Plates
from flask import Flask
from flask_restful import Api
from routes.home import Welcome
from database.plates import plates


app = Flask(__name__)
api = Api(app)
# our database
plates.populatePlates()

api.add_resource(Welcome, '/')

# get all plates
api.add_resource(Plates, '/plates/')
# get a plate by id
api.add_resource(Plate, '/plates/<string:id>/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)