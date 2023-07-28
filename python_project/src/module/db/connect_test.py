from mysqlConnector import MysqlConnector
import dataManipulation

class testMy:
    def __init__(self):
        self.conn = MysqlConnector('python')
        self.conn.connect()

    def main(self):
        ins = dataManipulation.DataManipulation(self.conn)
        sql = "select * from name_age_list order by id;"
        recs = ins.fetch_row(sql)
        print(recs)
ins = testMy()
ins.main()


