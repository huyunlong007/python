import pymysql

# 第一步：建立连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='HYL941128', database='mysql',
                       charset='utf8mb4')
# print(conn)
try:
    # 第二步：获得游标对象
    # cursor = conn.cursor()       #返回一个游标对象   这个对象可以执行sql语句
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:  # 将默认的输出元组改为输出为字典
        # 第三步：通过游标向数据库服务器发出sql语句，获取执行结果
        sql = "CREATE TABLE student(title  CHAR(20),sec_title  CHAR(20),content  VARCHAR(6499));"
        cursor.execute(sql)

        into = "INSERT INTO student(title,sec_title,content) VALUES (%s,%s, %s);"
        values =(4, 'white', 28)
        cursor.execute(into, values)
        # 第四步：提交上面的操作
        conn.commit()
except pymysql.MySQLError as err:
    # 第四步：回滚（提交失败）  不需要增删改时，不使用回滚
    conn.rollback()
finally:
    # 关闭连接（释放资源）
    conn.close()


