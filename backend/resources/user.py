from flask_restful import Resource, reqparse
from mock_data.query import query_db

connected = False
class User(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str) #Returns a specific user by specified by id
        args = parser.parse_args()
        if args["user"]:
            select_statement = "SELECT * FROM User WHERE `id` = {}".format(args["user"])
            return query_db(select_statement,connected)
        select_statement = "SELECT * FROM User"
        return query_db(select_statement,connected)
    def post(self):
        return
    def put(self, user_id):
        return
    def delete(self, user_id):
        return