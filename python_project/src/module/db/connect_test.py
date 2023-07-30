from mysqlConnector import MysqlConnector
from dataManipulation import DataManipulation as DataManipulation

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
        except Exception:
            print("メイン関数でエラー")
        finally:
            self.conn.close()
ins = testMy()
ins.main()


