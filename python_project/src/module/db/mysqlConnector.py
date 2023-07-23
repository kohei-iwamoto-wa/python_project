import mysql.connector as mySQLConn
from dbConnector import DbConnector
# from mysql.connector import errorCode

db_config = {
    'python' : {
        'user': 'docker',
        'password': 'docker',
        'host': '192.168.2.2',
        'database': 'python',
    },
}

class MysqlConnector(DbConnector):
    def __init__(self, db):
        self.conf = db_config[db]

    def connect(self):
        try:
            conn = mySQLConn.connect(**self.conf)
            print(conn.is_connected())
            return conn
        except Exception:
            raise