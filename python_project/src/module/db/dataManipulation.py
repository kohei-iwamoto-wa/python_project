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
            # culumn = ','.join(culumns)
            # tuple_count = len(values)
            # place_holder = list()
            # for _ in range(tuple_count):
            #     place_holder.append("%s")
            # place_holder = ','.join(place_holder)
            # self.conn.autocommit = True
            cur = self.conn.cursor()
            # str_sql = "INSERT INTO {table} ({culumn}) VALUES ({value});".format(
            #         table=table, culumn=culumn, value=place_holder)    
            # print(str_sql,type(values))
            str_sql = "INSERT INTO name_age_list (name, age) VALUES ('fuji',12);"
            cur.execute(str_sql)
            self.conn.commit()
            # cur.execute(str_sql, values)
        except Exception as e:
            print(type(e))
            raise

    def bulk_insert(self, values):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def transaction(self):
        pass