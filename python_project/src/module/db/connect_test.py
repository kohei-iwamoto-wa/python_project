from mysqlConnector import MysqlConnector
from dataManipulation import DataManipulation
import util.logManager.logManager as logger

class testMy:
    def __init__(self):
        self.conn = MysqlConnector('python')
        self.conn.connect()

    def main(self):
        try:
            ins = DataManipulation(self.conn)
            sql = "select * from name_age_list order by id;"
            recs = ins.fetch_rows(sql)
            ins = DataManipulation(self.conn)
            ins.insert('name_age_list', ('name', 'age'), ('koei', 32))
        except Exception as e:
            logger.error_log(e)
            print("メイン関数でエラー")
        finally:
            self.conn.close()
ins = testMy()
ins.main()


