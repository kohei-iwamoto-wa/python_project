from mysqlConnector import MysqlConnector
import dataManipulation.DataManipulation as DataManipulation

class testMy:
    def __init__(self):
        self.conn = MysqlConnector('python')
        self.conn.connect()

    def main(self):
        ins = DataManipulation(self.conn)
        sql = "select * from name_age_list order by id;"
        recs = ins.fetch_row(sql)
        ins.insert('name_age_list', ('name', 'age'), ('kohei', 32))
ins = testMy()
ins.main()


