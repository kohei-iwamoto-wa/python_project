from mysqlConnect import MysqlConnect

db_config = {
    'user': 'docker',
    'password': 'docker',
    'host': '192.168.2.2',
    'database': 'python'
}

class testMy:
    def __init__(self):
        self.conn = MysqlConnect(db_config)
        self.conn.connect()

    def main(self):
        pass
            
ins = testMy()
ins.main()


