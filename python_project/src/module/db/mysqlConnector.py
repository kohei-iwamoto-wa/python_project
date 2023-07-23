import dbConfig as conf
import mysql.connector as mySQLConn
from dbConnector import DbConnector

class MysqlConnector(DbConnector):
    def __init__(self, db):
        self.conf = conf.MYSQL_DEF[db]

    def connect(self):
        try:
            conn = mySQLConn.connect(**self.conf)
            print(conn.is_connected())
            return conn
        except Exception as e:
            print(e)
            raise