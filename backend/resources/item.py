from flask_restful import Resource, reqparse, request
from mock_data.query import query_db

connected = False
class Item(Resource):
    def get(self): #Currently all booleans return 0 or 1, not sure if this will be an issue
        parser = reqparse.RequestParser()
        parser.add_argument('item', type=str) #Returns a specific user by specified by id
        args = parser.parse_args()
        if args["item"]:
            select_statement = "SELECT * FROM Item WHERE `id` = {}".format(args["item"])
            return query_db(select_statement,connected)
        select_statement = "SELECT * FROM Item"
        return query_db(select_statement,connected), 200
    def post(self):
        insert_items = "INSERT INTO `Item` (`item_name`,`price`,`quantity`,`status`,`instock`,`sell`,`rent`) VALUES ('{}', {}, {}, '{}', {}, {}, {})"
        
        try:
            name = request.json["item_name"]
            price = request.json["price"]
            quantity = request.json["quantity"]
            status = request.json["status"]
            instock = request.json["instock"]
            sell = request.json["sell"]
            rent = request.json["rent"]
        except KeyError as e:
            return "No Key provided for:{}".format(e),400
            
        insert_statement = insert_items.format(name, price, quantity, status, instock, sell, rent)
        return query_db(insert_statement, connected), 201
    def put(self, item_id):
        update_item = "UPDATE `Item` SET `item_name` = '{}', `price` = {}, `quantity` = {}, `status` = '{}', `instock` = {}, `sell` = {}, `rent` = {} WHERE `id` = {}"
        try:
            name = request.json["item_name"]
            price = request.json["price"]
            quantity = request.json["quantity"]
            status = request.json["status"]
            instock = request.json["instock"]
            sell = request.json["sell"]
            rent = request.json["rent"]
        except KeyError as e:
            return "No Key provided for:{}".format(e),400
        
        update_statement = update_item.format(name, price, quantity, status, instock, sell, rent, item_id)
        return query_db(update_statement, connected), 204
    def delete(self, item_id):
        delete_item = "DELETE FROM `Item` WHERE `id` = {}"
        delete_statement = delete_item.format(item_id)
        try:
            query_db(delete_statement, connected)
            return "",204
        except Exception as e:
            return "An Error Occured:{}".format(e)