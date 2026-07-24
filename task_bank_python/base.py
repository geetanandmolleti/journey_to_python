# from pin import bank3
# from create import create_bank_user
# from balance_checker import bank4
# from depo import bank5
# from withdraw import bank6
# from transaction import bank7

# if __name__ == "__main__":
#     print("--- Step 1: Create a New User ---")
#     user_name = input("Enter user name: ")
#     user_dob = input("Enter date of birth (DD-MM-YYYY): ")

#     user1 = create_bank_user(name=user_name, dob=user_dob)

#     print("\nCreated user successfully!")
#     print("User ID:", user1.id)
#     print("User Name:", user1.name)
#     print("Account Number:", user1.acc_num)
#     print("Balance:", user1.bal)

#     print("\n--- Step 2: Generate/Update PIN ---")
#     bank3.pin_generation(user_id=user1.id)

#     print("\n--- Step 3: Check Account Balance ---")
#     bank4.get_account_balance(user1.acc_num)
#     print("\n--- Step 4: Deposit Money ---")
#     deposit_pin = (input("Enter your secret PIN: ").replace("'", "").replace('"', "").strip())
#     amount = float(input("Enter the value to deposit: "))

  
#     bank5.deposit(user1.acc_num, amount, deposit_pin)
#     print("\n--- Step 5: Withdraw Money ---")
#     withdraw_pin = (
#         input("Enter your secret PIN: ").replace("'", "").replace('"', "").strip()
#     )
#     withdraw_amount = float(input("Enter the value to withdraw: "))

#     bank6.withdraw(user1.acc_num, withdraw_amount, withdraw_pin)
#     print("\n--- Step 6: Transfer Money ---")
#     receiver_acc = input("Enter receiver account number: ").strip()
#     transfer_pin = (input("Enter your secret PIN: ").replace("'", "").replace('"', "").strip())
#     transfer_amount = float(input("Enter the amount to transfer: "))

#     bank7.transfer(user1.acc_num, receiver_acc, transfer_amount, transfer_pin)







from pin import bank3
from create import create_bank_user
from balance_checker import bank4
from depo import bank5
from withdraw import bank6
from transaction import bank7


while True:
    print("\nWelcome to  Bank of Asgard")
    print("1) Account creation")
    print("2) Set PIN")
    print("3) Check balance")
    print("4) Deposit")
    print("5) Withdraw amount")
    print("6) Account to account transfer")
    print("7) Exit")

    op = input("Select the option: ").strip()

    if op == "1":
        print("\n--- Account Creation ---")
        user_name = input("Enter user name: ")
        user_dob = input("Enter date of birth (DD-MM-YYYY): ")

        user1 = create_bank_user(name=user_name, dob=user_dob)

        print("\nCreated user successfully!")
        print("User ID:", user1.id)
        print("User Name:", user1.name)
        print("Account Number:", user1.acc_num)
        print("Balance:", user1.bal)

    elif op == "2":
        print("\n--- Set / Generate PIN ---")
        user_id = input("Enter user ID: ").strip()
        bank3.pin_generation(user_id=user_id)

    elif op == "3":
        print("\n--- Check Account Balance ---")
        acc_num = input("Enter account number: ").strip()
        bank4.get_account_balance(acc_num)

    elif op == "4":
        print("\n--- Deposit Money ---")
        acc_num = input("Enter account number: ").strip()
        deposit_pin = (input("Enter your secret PIN: ").replace("'", "").replace('"', "").strip())
        amount = float(input("Enter the value to deposit: "))
        bank5.deposit(acc_num, amount, deposit_pin)

    elif op == "5":
        print("\n--- Withdraw Money ---")
        acc_num = input("Enter account number: ").strip()
        withdraw_pin = (input("Enter your secret PIN: ").replace("'", "").replace('"', "").strip())
        withdraw_amount = float(input("Enter the value to withdraw: "))
        bank6.withdraw(acc_num, withdraw_amount, withdraw_pin)

    elif op == "6":
        print("\n--- Account to Account Transfer ---")
        sender_acc = input("Enter your account number: ").strip()
        receiver_acc = input("Enter receiver account number: ").strip()
        transfer_pin = ( input("Enter your secret PIN: ").replace("'", "").replace('"', "").strip())
        transfer_amount = float(input("Enter the amount to transfer: "))
        bank7.transfer(sender_acc, receiver_acc, transfer_amount, transfer_pin)

    elif op == "7":
        print("Thank you for visiting ABC Bank.")
        break

    else:
        print("Invalid option. Please select a valid choice.")