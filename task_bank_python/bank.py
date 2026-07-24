import sqlite3
connection= sqlite3.connect('bank.db')
cursor=connection.cursor()
# columns created----> name ,pin, acc_num,adress,dob,phn_no,father_name,aadhar,bal,id
# cursor.execute("DROP TABLE my_table;")
# cursor.execute("CREATE TABLE my_table (id INTEGER PRIMARY KEY,name VARCHAR(20),pin VARCHAR(64) DEFAULT '0000',acc_num BIGINT,adress VARCHAR(50),dob VARCHAR(10),phn_no BIGINT,father_name VARCHAR(20),aadhar BIGINT,bal INT DEFAULT 1000);")
# sql = "INSERT INTO my_table (name, acc_num) VALUES (?, ?);"
# values = ("user1", 123456789)
# cursor.execute(sql, values)
# connection.commit()