import mysql.connector
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'hagz'
}

def set_database(query, values):
    try:
        db = mysql.connector.connect(**mysql_config)
        #A cursor is an object that allows you to interact with the database.
        #  It acts as a pointer to the result set of a query
        cursor = db.cursor()
        cursor.execute(query, values)
        db.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def get_database(query):
    try:
        db = mysql.connector.connect(**mysql_config)
        #A cursor is an object that allows you to interact with the database.
        #  It acts as a pointer to the result set of a query
        cursor = db.cursor()
        cursor.execute(query)
        retrieved_data = cursor.fetchall()
        return retrieved_data
    except Exception as e:
        print(e)
    finally:
        cursor.close()


def edit_database(query):
    try:
        db = mysql.connector.connect(**mysql_config)
        #A cursor is an object that allows you to interact with the database.
        #  It acts as a pointer to the result set of a query
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()