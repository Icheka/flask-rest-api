from database.Plates import populatePlates
from routes.Index import Plate, Plates, Welcome
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
populatePlates()

# routes
'''
Our objective is to have CRUD endpoints for:
Adding a new plate             (Create)
Getting data from our database (Read)
Updating data in our database  (Update)
Deleting data from our database(Delete)
'''

# GET index route -> return welcome message
api.add_resource(Welcome, '/')
# GET /plates -> return all plates in database
api.add_resource(Plates, '/plates')
# GET /plates/1 -> find a specific plate by its ID and return it
api.add_resource(Plate, '/plates/<string:id>')

# POST /plates -> create a new plate

if __name__ == '__main__':
    app.run(debug=True, port=5000)
