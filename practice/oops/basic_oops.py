#basics of oops
# class school:
#     s_name='geetanand molleti'
#     loc='vizag'
#     principle='shilpa kumari'
# student1=school()
# student2=school()
# print(student1.s_name)  # geetanand molleti
# student2.s_name='shirisha'
# print(student2.s_name)  # shirisha







# constructor in oops
# class Bank:
#     # The __init__ method sets up the starting balance for every new account
#     def __init__(self, initial_bal=0):
#         self.bal = initial_bal

#     # 'self' refers to the specific account object calling the method
#     def deposit(self, val):
#         self.bal += val


# # 1. Create the account and set the initial balance at the same time
# acc = Bank(1000)

# # 2. Deposit some money
# acc.deposit(500)

# # 3. Check the new balance
# print(acc.bal)  # Outputs: 1500










# constructor chining 
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.holder = account_holder
#         self.balance = balance
#         print(f"Base account created for {self.holder}")


# # SavingsAccount inherits from BankAccount
# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, balance, interest_rate):
#         # 🔗 The Chain: Call the parent class constructor first!
#         super().__init__(account_holder, balance)

#         # Now add the specialized feature for this child class
#         self.interest_rate = interest_rate
#         print(f"Savings feature unlocked: {self.interest_rate}% interest rate")


# # Creating a savings account triggers the chain
# my_savings = SavingsAccount("Alice", 5000, 2.5)







# object methods------>when we use self
# class Dog:
#     def __init__(self, name):
#         self.name = name  # Every dog gets a name

#     # This is a simple object method
#     def bark(self):
#         print(f"{self.name} says Woof!")

# # 1. Create the object
# my_dog = Dog("Buddy")
# # 2. Call the method on that object
# my_dog.bark()  # Outputs: Buddy says Woof!









# class methods------>when we use cls
# class Dog:
#     # This is a class variable shared by ALL dogs
#     species = "Canis lupus"

#     def __init__(self, name):
#         self.name = name

#     # Standard Object Method (Works on an individual dog)
#     def bark(self):
#         print(f"{self.name} says Woof!")

#     # 🌟 Class Method (Works on the entire Dog class)
#     @classmethod
#     def get_species(cls):
#         # 'cls' refers to the Dog class, allowing us to access 'cls.species'
#         return f"All dogs belong to the species: {cls.species}"


# # 1. You can call a class method without creating a single dog object!
# print(Dog.get_species())  # Outputs: All dogs belong to the species: Canis lupus

# # 2. You can still call it from an instance if you want
# my_dog = Dog("Buddy")
# print(my_dog.get_species())












# static method---->dont uses anything 
# class Calculator:
#     # A standard object method needs to know about the specific calculator
#     def __init__(self, brand):
#         self.brand = brand

#     # 🌟 Static Method: It just takes two numbers, adds them, and leaves.
#     # It doesn't care what brand the calculator is, or if a calculator even exists!
#     @staticmethod
#     def add(x, y):
#         return x + y


# # 1. You can call it directly using the Class name (no object creation needed)
# result = Calculator.add(5, 7)
# print(result)  # Outputs: 12

# # 2. You can also call it from an instance, though it still won't access instance data
# my_calc = Calculator("Texas Instruments")
# print(my_calc.add(10, 20))  # Outputs: 30