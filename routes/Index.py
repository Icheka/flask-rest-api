from database.Plates import plates, replacePlates
from flask_restful import Resource, reqparse

create_plate_args = reqparse.RequestParser()
create_plate_args.add_argument(
    "color", type=str, help="color is required", required=True)
create_plate_args.add_argument(
    "dimensions", type=str, help="dimensions is required", required=True)
create_plate_args.add_argument(
    "type", type=str, help="type is required", required=True)
create_plate_args.add_argument(
    "price", type=str, help="price is required", required=True)
create_plate_args.add_argument(
    "material", type=str, help="material is required", required=True)


class Welcome(Resource):
    def get(self):
        return 'Welcome to Koala Online Store'


class Plates(Resource):
    def get(self):
        return plates

    def post(self):
        args = create_plate_args.parse_args()
        args['id'] = str(len(plates) + 1)
        plates.append(args)
        return {'data': args}


class Plate(Resource):
    def get(self, id):
        for plate in plates:
            if plate['id'] == id:
                return {'type': 'Success', 'data': plate}
        return {'type': 'Error', 'message': 'No item found with that ID'}
