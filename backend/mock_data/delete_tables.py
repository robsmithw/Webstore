from query import query_db

connected = False
drop_item = "DROP TABLE `Item`"
drop_user = "DROP TABLE `User`"
drop_link = "DROP TABLE `Link`"

query_db(drop_link, connected)
query_db(drop_user, connected)
query_db(drop_item, connected)