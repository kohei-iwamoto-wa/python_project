"""データ操作クラス"""

class DataManipulation:
    def __init__(self, conn):
        self.conn = conn

    def iter(self, sql):
        try:
            cur = self.conn.cursor(buffered=True)
            cur.execute(sql)
            return cur
        except Exception as e:
            print(type(e))
            raise
        finally:
            cur.close()

    def select_all():
        try:
            cur = self.conn.cursor()
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print(type(e))
            raise
        finally:
            cur.close()
    
    def insert(self):
        pass

    def upload(self):
        pass

    def delete(self):
        pass

    def transaction(self):
        pass