import dbConfig as conf
import mysql.connector as mySQLConn
from dbConnector import DbConnector
# データベースコネクション管理
class MysqlConnector(DbConnector):
    def __init__(self, db):
        self.db_conf = conf.MYSQL_DEF[db]
        self.conn = None

    def connect(self):
        try:
            print("データベース接続する")
            self.conn = mySQLConn.connect(**self.db_conf)
            return self.conn
        except Exception as e:
            print(e)
            raise

    def cursor(self):
        try:
            print("カーソル生成")
            return self.conn.cursor()
        except Exception as e:
            print(e)
            raise

    def commit(self):
        try:
            print("テーブルにコミットする")
            return self.conn.commit()
        except Exception as e:
            print(e)
            raise

    def close(self):
        try:
            print("コネクションを閉じる")
            return self.conn.close()
        except Exception:
            print(e)
            raise