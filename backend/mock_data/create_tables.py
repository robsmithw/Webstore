from query import query_db

connected = False
create_item = "CREATE TABLE `Item` (" \
        "`id` int NOT NULL AUTO_INCREMENT," \
        "`item_name` varchar(50) NOT NULL," \
        "`price` int NOT NULL," \
        "`quantity` int NOT NULL," \
        "`status` varchar(20) NOT NULL," \
        "`instock` boolean NOT NULL," \
        "`sell` boolean NOT NULL," \
        "`rent` boolean NOT NULL," \
        "PRIMARY KEY(`id`) )"
create_user = "CREATE TABLE `User` (" \
        "`id` int NOT NULL AUTO_INCREMENT," \
        "`user_name` varchar(50) NOT NULL," \
        "`password` varchar(64) NOT NULL," \
        "PRIMARY KEY(`id`) )"
create_link = "CREATE TABLE `Link` (" \
        "`item_id` int NOT NULL," \
        "`current_user_id` int NOT NULL," \
        "`new_user_id` int," \
        "PRIMARY KEY(`item_id`)," \
        "FOREIGN KEY(`item_id`) REFERENCES Item(`id`)," \
        "FOREIGN KEY(`current_user_id`) REFERENCES User(`id`) )"
query_db(create_item, connected)
query_db(create_user, connected)
query_db(create_link, connected)