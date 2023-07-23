import mysql.connector as mySQLConn
from dbConnector import DbConnector
# from mysql.connector import errorCode

db_config = {
    'user': 'docker',
    'password': 'docker',
    'host': '192.168.2.2',
    'database': 'python'
}

class MysqlConnector(DbConnector):
    def __init__(self):
        pass

    def connect(self):
        try:
            conn = mySQLConn.connect(**db_config)
            print(conn.is_connected())
            return conn
        except Exception:
            raise