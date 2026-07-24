# method over riding
# Parent Class
# class Animal:
#     def make_sound(self):
#         print("The animal makes a generic sound.")


# # Child Class overriding the parent method
# class Dog(Animal):
#     def make_sound(self):
#         print("🐶 Woof! Woof!")


# # Another Child Class overriding the parent method
# class Cat(Animal):
#     def make_sound(self):
#         print("🐱 Meow!")
# generic_animal = Animal()
# rex = Dog()
# whiskers = Cat()

# generic_animal.make_sound()  # Outputs: The animal makes a generic sound.
# rex.make_sound()  # Outputs: 🐶 Woof! Woof! (Overridden)
# whiskers.make_sound()  # Outputs: 🐱 Meow! (Overridden)











# method overloading(simulation only possible)
# class FlexibleCalculator:
#     def calc(self, *args):
#         # We can perform different logic based on how many arguments were passed
#         if len(args) < 2:
#             return "Error: Please provide at least 2 numbers to add."

#         # Sums up all the numbers passed into args
#         return sum(args)


# # Testing the dynamic calculator
# flex_calc = FlexibleCalculator()

# print(flex_calc.calc(10))  # Outputs: Error: Please provide at least 2 numbers to add.
# print(flex_calc.calc(10, 20))  # Outputs: 30
# print(flex_calc.calc(1, 2, 3, 4))  # Outputs: 10


















# operator overloading
# class Number:
#     def __init__(self, val):
#         self.val = val

#     # Overloading '+'
#     def __add__(self, other):
#         return self.val + other.val


# # Test it out
# num1 = Number(10)
# num2 = Number(20)

# print(num1 + num2)  # Outputs: 30






# duck taping
# class Dog:
#     def sound(self):
#         return "Bark!"


# class Car:
#     def sound(self):
#         return "Honk!"


# # This function just grabs whatever is given to it and calls .sound()
# def make_noise(thing):
#     print(thing.sound())


# # Python runs both without complaining, even though dogs and cars are totally different!
# make_noise(Dog())  # Outputs: Bark!
# make_noise(Car())  # Outputs: Honk!












# monkey patching
# class Robot:
#     def speak(self):
#         return "Hello, human."


# # 1. Normal behavior
# bot = Robot()
# print(bot.speak())  # Outputs: Hello, human.


# # 2. THE MONKEY PATCH: We define a brand new function
# def broken_voice(self):
#     return "Bzzt... Error... Hello!"


# # 3. We overwrite the original speak method with our new one
# Robot.speak = broken_voice


# # 4. Now, the exact same code behaves differently
# print(bot.speak())  # Outputs: Bzzt... Error... Hello!