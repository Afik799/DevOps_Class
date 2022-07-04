import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='P0PvfGbwKl', passwd='BvZW0m8DXo')
conn.autocommit(True)

cursor = conn.cursor()
cursor.execute("INSERT into P0PvfGbwKl.myTable (name, id) VALUES ('AFIK', 55)") ## inserts values to the table
# cursor.execute("UPDATE P0PvfGbwKl.myTable SET id = '10' WHERE name = 'AFIK'") ## updates values

# cursor.execute("SELECT * FROM P0PvfGbwKl.myTable;") ## selecting the all values (*) from table
#
# # Iterating table and printing all users
# for row in cursor:
#     print(row)
#     print(cursor)


cursor.close()
conn.close()
