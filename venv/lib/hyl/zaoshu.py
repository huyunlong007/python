cur = conn.cursor()
sql = """CREATE TABLE xiaoshuo(
                 title  CHAR(20),
                 sec_title  CHAR(20),
                 content  VARCHAR(6499))"""
cur.execute(sql)
conn.commit()


