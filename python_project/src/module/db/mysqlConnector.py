import mysql.connector as mySQLConn
from dbConnector import DbConnector
# from mysql.connector import errorCode

class MysqlConnect(DbConnector):
    def __init__(self, conn_info):
        print(conn_info)
        self.conn_info = conn_info

    def connect(self):
        try:
            conn = mySQLConn.connect(**self.conn_info)
            print(conn.is_connected())
            return conn
        except Exception:
            raise