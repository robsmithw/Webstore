from query import query_db

connected = False
load_items = ["INSERT INTO `Item` (`price`,`quantity`,`status`,`instock`"\
",`sell`,`rent`) VALUES (12, 1, 'New', true, true, false)",
"INSERT INTO `Item` (`price`,`quantity`,`status`,`instock`"\
",`sell`,`rent`) VALUES (10, 11, 'Used', false, false, true)"]
load_users = ["INSERT INTO `User` (`user_name`,`password`)"\
" VALUES ('Robert_user_name','some_password')",
"INSERT INTO `User` (`user_name`,`password`)"\
" VALUES ('John_user_name','another_password')"]
load_links = ["INSERT INTO `Link` (`item_id`,`current_user_id`,`new_user_id`)"\
" VALUES (1, 1, NULL)",
"INSERT INTO `Link` (`item_id`,`current_user_id`,`new_user_id`)"\
" VALUES (2, 2, 1)"]

for item in load_items:
    query_db(item, connected)
for user in load_users:
    query_db(user, connected)
for link in load_links:
    query_db(link, connected)