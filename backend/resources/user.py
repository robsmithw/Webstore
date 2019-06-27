from flask_restful import Resource, reqparse, request
from mock_data.query import query_db

connected = False
class User(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int) #Returns a specific user by specified by id
        parser.add_argument('user', type=str) #Returns a specific user by user_name
        args = parser.parse_args()
        if args["id"]:
            select_statement = "SELECT * FROM User WHERE `id` = {}".format(args["id"])
            return query_db(select_statement,connected)
        if args["user"]:
            select_statement = "SELECT * FROM User WHERE `user_name` = {}".format(args["user"])
            return query_db(select_statement,connected)
        select_statement = "SELECT * FROM User"
        return query_db(select_statement,connected), 200
    def post(self): #Need to look into hashing passwords using pbkdf2_hmac
        insert_users = "INSERT INTO `User` (`user_name`,`password`) VALUES ('{}', '{}')"

        try:
            name = request.json["user_name"]
            user_pass = request.json["password"]
        except KeyError as e:
            return "No Key provided for:{}".format(e),400

        insert_statement = insert_users.format(name,user_pass)
        return query_db(insert_statement, connected), 201
    def put(self, user_id):
        update_users = "UPDATE `User` SET `user_name` = '{}', `password` = '{}' WHERE `id` = {}"
        try:
            name = request.json["user_name"]
            user_pass = request.json["password"]
        except KeyError as e:
            return "No Key provided for:{}".format(e),400
        
        update_statement = update_users.format(name, user_pass, user_id)
        return query_db(update_statement, connected), 204
    def delete(self, user_id):
        return