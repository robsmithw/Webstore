from query import query_db
import json

connected = False
insert_users = "INSERT INTO `User` (`user_name`,`password`) VALUES ('{}', '{}')"
insert_items = "INSERT INTO `Item` (`item_name`,`price`,`quantity`,`status`,`instock`,`src`,`sell`,`rent`) VALUES ('{}', {}, {}, '{}', {}, '{}', {}, {})"
insert_links = "INSERT INTO `Link` (`item_id`,`current_user_id`,`new_user_id`) VALUES ({}, {}, {})"

with open("users.json", 'r') as json_file:
	all_users = json.load(json_file)
for user in all_users["Users"]:
    name = user["user_name"]
    user_pass = user["password"]
    insert_statement = insert_users.format(name, user_pass)
    query_db(insert_statement,connected)

with open("items.json", 'r') as json_file:
	all_items = json.load(json_file)
for item in all_items["for_sell"]:
    name = item["item_name"]
    price = item["price"]
    quantity = item["quantity"]
    status = item["status"]
    instock = item["instock"]
    src = item["src"]
    sell = item["sell"]
    rent = item["rent"]
    insert_statement = insert_items.format(name,price,quantity,status,instock,src,sell,rent)
    query_db(insert_statement,connected)