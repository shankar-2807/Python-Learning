import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1137',
    database = 'fbs'
)

cursor = conn.cursor()
sql = 'drop database fbs'
cursor.execute(sql)
# print(conn)
cursor.close()
conn.close()