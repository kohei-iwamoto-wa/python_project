import dbConfig as conf
import mysql.connector as mySQLConn
from dbConnector import DbConnector

class MysqlConnector(DbConnector):
    def __init__(self, db):
        self.db_conf = conf.MYSQL_DEF[db]

    def connect(self):
        try:
            return mySQLConn.connect(**self.db_conf)
        except Exception as e:
            print(e)
            raise
