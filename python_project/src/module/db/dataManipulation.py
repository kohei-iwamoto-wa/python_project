"""データ操作クラス

SQL文を挿入して使用する。
SQLを挿入際は、サニタイザーを利用すること。
"""

# import util.checkInput as CheckInput 

class DataManipulation:
    def __init__(self, conn):
        self.conn = conn

    def fetch_rows(self, sql):
        """"SQLベタがき"""
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            recs = []
            for row in cur:
                recs.append(row)
        except Exception as e:
            print("Error:", e)
        return recs
    
    def insert(self, table, culumns, values):
        """レコード登録"""
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
            cur = self.conn.cursor()
            cur.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            raise

    def execute_sql(self, sql):
        """更新削除"""
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            raise
