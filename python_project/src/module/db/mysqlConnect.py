# import mysql.connector as DbCon
# from mysql.connector import errorcode

class MysqlConnect:
    def __init__(self, conf):
        self.conf = conf

    def connect(self):
        try:
            print("こんにちは、世界")
            # db_con = DbCon()
            # con = db_con.connect(self.conf)
            # print(conn.is_connected())
            # return con
        except Exception:
            raise