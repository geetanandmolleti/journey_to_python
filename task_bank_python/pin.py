import hashlib
import sqlite3
from main import Bank


class bank3(Bank):
    @staticmethod
    def pin_generation(name=None, dob=None, acc_num=None, user_id=None):
        connection = sqlite3.connect("bank.db")
        cursor = connection.cursor()

        if user_id is not None:
            user = cursor.execute(
                "SELECT id FROM my_table WHERE id = ?", (user_id,)
            ).fetchone()
        elif acc_num is not None:
            user = cursor.execute(
                "SELECT id FROM my_table WHERE acc_num = ?", (acc_num,)
            ).fetchone()
        else:
            user = cursor.execute(
                "SELECT id FROM my_table WHERE name = ? AND dob = ?",
                (name, dob),
            ).fetchone()

        if user:
            res = input("enter your pin: ").strip()

            if not res.isdigit() or len(res) != 4:
                print("PIN must be a 4-digit number.")
                connection.close()
                return

            hashed_pin = hashlib.sha256(str(res).encode()).hexdigest()

            cursor.execute(
                "UPDATE my_table SET pin = ? WHERE id = ?",
                (hashed_pin, user[0]),
            )
            connection.commit()
            print("PIN successfully updated!")
        else:
            print("User not found with the provided details.")

        connection.close()


