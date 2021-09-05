from flask_restful import Resource


class Welcome(Resource):
    def get(self):
        return 'Welcome to Koala Online Store'