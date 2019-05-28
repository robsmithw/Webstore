from flask_restful import Resource
from mock_data.query import query_db

connected = False
class Item(Resource):
    def get(self):
        return query_db("SELECT * FROM Item",connected)
    def post(self):
        return
    def put(self, item_id):
        return
    def delete(self, item_id):
        return