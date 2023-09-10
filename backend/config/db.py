import mysql.connector as connector

def getDBConnection(config_data):
    try:
        conn = connector.connect(
            host=str(config_data["HOSTNAME"]), 
            user=str(config_data["USERNAME"]),
            password = str(config_data["PASSWORD"]),
            database=str(config_data["DATABASE"])
        )
        conn.autocommit = True
        return conn
    except Exception as e:
        print("Error: %s" % (e,))