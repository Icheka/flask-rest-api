from flask_restful import Resource, reqparse
from database.plates import plates

create_plate_body = reqparse.RequestParser()
create_plate_body.add_argument("color", type=str, required=True, help="color is required")
create_plate_body.add_argument("dimensions", type=str, required=True, help="dimensions is required")
create_plate_body.add_argument("type", type=str, required=True, help="type is required")
create_plate_body.add_argument("price", type=float, required=True, help="price is required")
create_plate_body.add_argument("material", type=str, required=True, help="material is required")



class Plates(Resource):
    def get(self):
        # return all plates
        return plates.plates

    def post(self):
        body = create_plate_body.parse_args()
        # create a new id
        body['id'] = str(len(plates.plates) + 1)
        # add the new plate to our plates array
        plates.plates.append(body)
        return body

class Plate(Resource):
    def get(self, id):
        for plate in plates.plates:
            if plate['id'] == id:
                return plate
        return "No plate was found with that ID"
    def put(self, id):
        # find the plate by the given id
        body = create_plate_body.parse_args()

        res = plates.updateAtId(int(id), body)
        if res == True:
            return "Successful"
        else:
            return "Plate with that ID was not found"