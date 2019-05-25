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
        if(not is_connected):
            password = (str(sys.argv[1])) #We have user provide password for super_user through command line
            our_connection = test_connect(password,is_connected)

    except IndexError:
        print("Please ensure you're providing the password for super_user through command line.")
        exit(0)

    try:
        success = True
        with our_connection.cursor() as cursor:
            cursor.execute(sql_statement)
            if("SELECT" in sql_statement):
                results = cursor.fetchone()
                print(results)
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