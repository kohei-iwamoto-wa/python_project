"""データ操作クラス

SQL文を挿入して使用する。
SQLを挿入際は、サニタイザーを利用すること。
"""

class DataManipulation:
    def __init__(self, conn, tables=None):
        self.conn = conn

    def fetch_row(self, sql):
        """"SQLベタがき"""
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            recs = []
            for row in cur:
                recs.append(row)
        except Exception as e:
            print("Error:", e)
        finally:
            self.conn.close()
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
        finally:
            self.conn.close()
    
    def insert(self, table, culumns, values, is_bulk=True):
        """テーブルに1レコードずつ登録する"""
        try:
            culumn = ','.join(culumns)
            tuple_count = len(values)
            place_holders = list()
            # カラム数分%sを生成
            for _ in range(tuple_count):
                place_holders.append('%s')
            place_holders = ','.join(place_holders)
            sql = "INSERT INTO {table} ({culumn}) VALUES ({value});".format(
                    table=table, culumn=culumn, value=place_holders)
            if not is_bulk:
                cur = self.conn.cursor()
                cur.execute(sql, values)
            else:
                with self.conn.cursor() as cur:
                    cur.executemany(sql, values)
            self.conn.commit()
        except Exception as e:
            print(type(e))
            raise
        finally:
            self.conn.close()

    def update(self, values):
        try:
            # sql = "UPDATE {table} SET {culumns} = {data} ".format(table=table,culumns=culumns,data)
        except Exception as e
            print(e)
            raise
        finally:
            self.conn.close()

    def delete(self):
        pass
