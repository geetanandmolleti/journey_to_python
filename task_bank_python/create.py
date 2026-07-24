# import sqlite3
# from main import Bank


# class bank2(Bank):
#     @staticmethod
#     def create(
#         name,
#         acc_num,
#         pin="0000",
#         address=None,
#         dob=None,
#         phn_no=None,
#         father_name=None,
#         aadhar=None,
#         bal=1000,
#     ):
#         connection = sqlite3.connect("bank.db")
#         cursor = connection.cursor()

#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS my_table (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name VARCHAR(20),
#                 pin VARCHAR(64) DEFAULT '0000',
#                 acc_num BIGINT,
#                 adress VARCHAR(50),
#                 dob VARCHAR(10),
#                 phn_no BIGINT,
#                 father_name VARCHAR(20),
#                 aadhar BIGINT,
#                 bal INT DEFAULT 1000
#             );
#         """)

#         sql = "INSERT INTO my_table (name, pin, acc_num, adress, dob, phn_no, father_name, aadhar, bal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
#         values = (name, pin, acc_num, address, dob, phn_no, father_name, aadhar, bal)

#         cursor.execute(sql, values)
#         connection.commit()

#         new_id = cursor.lastrowid

#         connection.close()

#         # Returns a bank2 instance instead of hardcoded Bank
#         return bank2(
#             name, acc_num, bal, pin, address, dob, phn_no, father_name, aadhar, new_id
#         )








import random
import sqlite3
from main import Bank


def create_bank_user(
    name,
    acc_num=None,
    pin="0000",
    address=None,
    dob=None,
    phn_no=None,
    father_name=None,
    aadhar=None,
    bal=1000,
):
    if acc_num is None:
        acc_num = random.randint(100_000_000, 999_999_999)

    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20),
            pin VARCHAR(64) DEFAULT '0000',
            acc_num BIGINT,
            adress VARCHAR(50),
            dob VARCHAR(10),
            phn_no BIGINT,
            father_name VARCHAR(20),
            aadhar BIGINT,
            bal INT DEFAULT 1000
        );
    """
    )

    sql = "INSERT INTO my_table (name, pin, acc_num, adress, dob, phn_no, father_name, aadhar, bal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
    values = (name, pin, acc_num, address, dob, phn_no, father_name, aadhar, bal)

    cursor.execute(sql, values)
    connection.commit()

    new_id = cursor.lastrowid
    connection.close()

    return Bank(
        name, acc_num, bal, pin, address, dob, phn_no, father_name, aadhar, new_id
    )