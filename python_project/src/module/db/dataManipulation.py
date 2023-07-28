"""データ操作クラス

SQL文を挿入して使用する。
SQLを挿入際は、サニタイザーを利用すること。
"""

class DataManipulation:
    def __init__(self, conn):
        self.conn = conn

    def fetch_row(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            recs = []
            for row in cur:
                recs.append(row)
        except Exception as e:
            print("Error:", e)
        finally:
            cur.close()
        return recs
    
    def select_all(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
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