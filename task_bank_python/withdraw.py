import hashlib
import sqlite3


class bank6:
    @staticmethod
    def clean_pin(pin_value):
        if pin_value is None:
            return ""
        pin_str = str(pin_value).strip()
        pin_str = pin_str.replace("'", "").replace('"', "").replace(" ", "")
        return pin_str

    @staticmethod
    def withdraw(acc_num, amount, entered_pin, db_path="bank.db"):
        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than 0.")
            return False

        user_pin = bank6.clean_pin(entered_pin)
        hashed_user_pin = hashlib.sha256(user_pin.encode()).hexdigest()
        acc_num = str(acc_num).strip()

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT bal, pin FROM my_table WHERE acc_num = ?",
            (acc_num,),
        )
        row = cursor.fetchone()

        if row is None:
            print("Account number not found!")
            conn.close()
            return False

        current_balance = row[0]
        db_pin = bank6.clean_pin(row[1])

        if hashed_user_pin != db_pin:
            print("Incorrect PIN! Transaction cancelled.")
            conn.close()
            return False

        if current_balance < amount:
            print(f"Insufficient funds! Current balance: ₹{current_balance}")
            conn.close()
            return False

        new_balance = current_balance - amount
        cursor.execute(
            "UPDATE my_table SET bal = ? WHERE acc_num = ?",
            (new_balance, acc_num),
        )
        conn.commit()

        print(f"Successfully withdrew ₹{amount}!")
        print(f"New Balance: ₹{new_balance}")

        conn.close()
        return True
