import mysqlConnect

class testMy:
    def __init__(self):
        MysqlConnect('root','root','127.0.0.1','world')

if '__name__' == '__main__':
    ins = testMy()

