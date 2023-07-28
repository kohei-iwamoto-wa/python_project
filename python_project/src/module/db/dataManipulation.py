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
    
    def insert(self, table, culumns, values):
        try:
            culumn = ','.join(culumns)
            value_count = len(values)
            place_holders = list()
            # カラム数分%sを生成
            for _ in range(tuple_count):
                place_holders.append('%s')
            place_holders = ','.join(place_holders)
            cur = self.conn.cursor()
            str_sql = "INSERT INTO {table} ({culumn}) VALUES ({value});".format(
                    table=table, culumn=culumn, value=place_holders)    
            cur.execute(str_sql, values)
            self.conn.commit()
        except Exception as e:
            print(type(e))
            raise
        finally:
            cur.close()

    def bulk_insert(self, values):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def transaction(self):
        pass