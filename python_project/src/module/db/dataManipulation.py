"""データクラス"""

class DataManipulation:
    def __init__(self, conn):
        self.conn = conn

    def iter(self):
        try:
            cur = self.conn.cursor()
            cur.execute(sql_str)
            return cur
        except Exception as e:
            print(type(e))
            raise
    
    def insert(self):
        pass

    def upload(self):
        pass

    def delete(self):
        pass

    def transaction(self):
        pass