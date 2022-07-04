import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='P0PvfGbwKl', passwd='BvZW0m8DXo')
conn.autocommit(True)

cursor = conn.cursor()

#2

# cursor.execute("INSERT into P0PvfGbwKl.dogs (name, age, breed) VALUES ('Max', 2, 'Bull Trier')")
# cursor.execute("INSERT into P0PvfGbwKl.dogs (name, age, breed) VALUES ('Dave', 4, 'Hotdog')")
# cursor.execute("INSERT into P0PvfGbwKl.dogs (name, age, breed) VALUES ('John', 8, 'Malinua')")

#3

cursor.execute("UPDATE P0PvfGbwKl.dogs SET age=5 WHERE name = 'Dave'")

#4

cursor.execute("DELETE from P0PvfGbwKl.dogs WHERE name = 'John'")

#5

cursor.execute("SELECT * FROM P0PvfGbwKl.dogs;")
for row in cursor:
    print(row)





cursor.close()
conn.close()
