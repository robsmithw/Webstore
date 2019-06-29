import pymysql
import sys

def test_connect(the_password,connection_status):
    connection = pymysql.connect(host='192.168.99.100',
            user='root',
            password=the_password,
            db='mysql',
            port=8000,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    print("connection Successful")
    connection_status = True
    return connection


def query_db(sql_statement,is_connected):
    try:
        if not is_connected:
            name_of_file = sys.argv[0]
            if './' in name_of_file:
                newstring = name_of_file.split('/')
                name_of_file = newstring[1]
            if name_of_file == 'create_tables.py' or name_of_file == 'load_tables.py' or name_of_file == 'delete_tables.py':
                with open("../password.txt",'r') as pass_file:
                    password = pass_file.readline()
            else:
                with open("password.txt",'r') as pass_file:
                    password = pass_file.readline()
            our_connection = test_connect(password,is_connected)

    except FileNotFoundError: #Need to eventually make sure this catch still works
        print("Please make sure you have a file to store the password")
        exit(0)

    try:
        success = True
        with our_connection.cursor() as cursor:
            cursor.execute(sql_statement)
            if("SELECT" in sql_statement):
                results = []
                for result in cursor.fetchall():
                    results.append(result)
                return results
        our_connection.commit()
    except Exception as e:
        success = False
        print("Exception Occured:{}".format(e))
    finally:
        if(success):
            print("Successfully executed query {}".format(sql_statement))
        else:
            print("Did not successfully execute query.")
        our_connection.close()