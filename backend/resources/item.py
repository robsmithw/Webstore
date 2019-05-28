from flask_restful import Resource, reqparse
from mock_data.query import query_db

connected = False
class Item(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('item', type=str) #Returns a specific user by specified by id
        args = parser.parse_args()
        if args["item"]:
            select_statement = "SELECT * FROM Item WHERE `id` = {}".format(args["item"])
            return query_db(select_statement,connected)
        select_statement = "SELECT * FROM Item"
        return query_db(select_statement,connected)
    def post(self):
        return
    def put(self, item_id):
        return
    def delete(self, item_id):
        return