from flask_restful import Resource, reqparse, request
from mock_data.query import query_db
from hashlib import pbkdf2_hmac

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
        return query_db(select_statement,connected), 200
    def post(self): #Need to look into hashing passwords using pbkdf2_hmac
        insert_users = "INSERT INTO `User` (`user_name`,`password`) VALUES ('{}', '{}')"
        name = request.json["user_name"]
        user_pass = request.json["password"]
        insert_statement = insert_users.format(name,user_pass)
        return query_db(insert_statement, connected), 201
    def put(self, user_id):
        return
    def delete(self, user_id):
        return