from mysqlConnector import MysqlConnector

class testMy:
    def __init__(self):
        self.conn = MysqlConnector('python')
        self.conn.connect()

    def main(self):
        pass
            
ins = testMy()
ins.main()


