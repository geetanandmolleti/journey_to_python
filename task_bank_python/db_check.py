from bank import connection, cursor

cursor.execute("SELECT * FROM my_table")
data = cursor.fetchall()

for row in data:
    print(row)
