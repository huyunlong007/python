cur = conn.cursor()
sql = """CREATE TABLE xiaoshuo(
                 title  CHAR(20),
                 sec_title  CHAR(20),
                 content  VARCHAR(6499))"""
cur.execute(sql)
conn.commit();

into = "INSERT INTO scrapy_yilong2(title,author,comment,`time`) VALUES (%s,%s, %s, %s)"
values = (item['title'],item['author'],item['comment'],item['time'])
cur.execute(into, values)
conn.commit()





