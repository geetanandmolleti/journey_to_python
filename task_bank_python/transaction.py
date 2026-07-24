import hashlib
import sqlite3


class bank7:
    @staticmethod
    def clean_pin(pin_value):
        if pin_value is None:
            return ""
        pin_str = str(pin_value).strip()
        pin_str = pin_str.replace("'", "").replace('"', "").replace(" ", "")
        return pin_str

    @staticmethod
    def transfer(sender_acc, receiver_acc, amount, sender_pin, db_path="bank.db"):
        if amount <= 0:
            print("Invalid amount! Transfer must be greater than 0.")
            return False

        sender_acc = str(sender_acc).strip()
        receiver_acc = str(receiver_acc).strip()

        if sender_acc == receiver_acc:
            print("Sender and receiver account numbers cannot be the same!")
            return False

        user_pin = bank7.clean_pin(sender_pin)
        hashed_user_pin = hashlib.sha256(user_pin.encode()).hexdigest()

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT bal, pin FROM my_table WHERE acc_num = ?", (sender_acc,)
            )
            sender_row = cursor.fetchone()

            if sender_row is None:
                print("Sender account number not found!")
                conn.close()
                return False

            sender_balance, db_pin = sender_row[0], bank7.clean_pin(sender_row[1])

            if hashed_user_pin != db_pin:
                print("Incorrect PIN! Transaction cancelled.")
                conn.close()
                return False

            if sender_balance < amount:
                print(f"Insufficient funds! Current balance: ₹{sender_balance}")
                conn.close()
                return False

            cursor.execute(
                "SELECT bal FROM my_table WHERE acc_num = ?", (receiver_acc,)
            )
            receiver_row = cursor.fetchone()

            if receiver_row is None:
                print("Receiver account number not found!")
                conn.close()
                return False

            receiver_balance = receiver_row[0]

            new_sender_bal = sender_balance - amount
            new_receiver_bal = receiver_balance + amount

            cursor.execute(
                "UPDATE my_table SET bal = ? WHERE acc_num = ?",
                (new_sender_bal, sender_acc),
            )
            cursor.execute(
                "UPDATE my_table SET bal = ? WHERE acc_num = ?",
                (new_receiver_bal, receiver_acc),
            )

            conn.commit()

            print(f"Successfully transferred ₹{amount} to Account {receiver_acc}!")
            print(f"Your New Balance: ₹{new_sender_bal}")

            conn.close()
            return True

        except Exception:
            conn.rollback()
            print(
                "Transaction failed due to a system error. Money was not transferred."
            )
            conn.close()
            return False
