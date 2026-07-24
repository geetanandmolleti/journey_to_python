# import sqlite3
# import random

# class Bank:
#     def __init__(self,name,acc_num, bal, pin, address, dob, phn_no, father_name, aadhar, user_id,):
        
#         self.id = user_id
#         self.name = name
#         self.acc_num = acc_num
#         self.bal = bal
#         self.pin = pin
#         self.address = address
#         self.dob = dob
#         self.phn_no = phn_no
#         self.father_name = father_name
#         self.aadhar = aadhar

#     # @staticmethod
#     # def create(
#     #     name,
#     #     acc_num,
#     #     pin="0000",
#     #     address=None,
#     #     dob=None,
#     #     phn_no=None,
#     #     father_name=None,
#     #     aadhar=None,
#     #     bal=1000,
#     # ):
#     #     connection = sqlite3.connect("bank.db")
#     #     cursor = connection.cursor()

#     #     cursor.execute("""
#     #         CREATE TABLE IF NOT EXISTS my_table (
#     #             id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #             name VARCHAR(20),
#     #             pin VARCHAR(64) DEFAULT '0000',
#     #             acc_num BIGINT,
#     #             adress VARCHAR(50),
#     #             dob VARCHAR(10),
#     #             phn_no BIGINT,
#     #             father_name VARCHAR(20),
#     #             aadhar BIGINT,
#     #             bal INT DEFAULT 1000
#     #         );
#     #     """)

#     #     sql = "INSERT INTO my_table (name, pin, acc_num, adress, dob, phn_no, father_name, aadhar, bal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
#     #     values = (name, pin, acc_num, address, dob, phn_no, father_name, aadhar, bal)

#     #     cursor.execute(sql, values)
#     #     connection.commit()

#     #     new_id = cursor.lastrowid

#     #     connection.close()

#     #     return Bank(
#     #         name, acc_num, bal, pin, address, dob, phn_no, father_name, aadhar, new_id
#     #     )

# name=input('enter user name')
# acc_num = random.randint(100_000_000, 999_999_999)
# print('account number is being generated',acc_num)
# user1 = Bank.create(name, acc_num)

# print("Created user successfully!")
# print("User ID:", user1.id)
# print("User Name:", user1.name)
# print("Account Number:", user1.acc_num)
# print("Balance:", user1.bal)








class Bank:
    def __init__(
        self,
        name,
        acc_num,
        bal,
        pin,
        address,
        dob,
        phn_no,
        father_name,
        aadhar,
        user_id,
    ):
        self.id = user_id
        self.name = name
        self.acc_num = acc_num
        self.bal = bal
        self.pin = pin
        self.address = address
        self.dob = dob
        self.phn_no = phn_no
        self.father_name = father_name
        self.aadhar = aadhar