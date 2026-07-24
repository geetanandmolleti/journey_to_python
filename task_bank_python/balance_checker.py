import sqlite3
from main import Bank


class bank4(Bank):
    @staticmethod
    def get_account_balance(acc_num):
        connection = sqlite3.connect("bank.db")
        cursor = connection.cursor()

        cursor.execute("SELECT bal, name FROM my_table WHERE acc_num = ?", (acc_num,))
        result = cursor.fetchone()

        connection.close()

        if result:
            balance, name = result
            print(f"Account Holder: {name}")
            print(f"Current Balance: ₹{balance}")
            return balance

        print("Account number not found.")
        return None
