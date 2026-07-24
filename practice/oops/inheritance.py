# # single level
# # 1. The Parent Class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

#     def sleep(self):
#         print(f"{self.name} is sleeping.")


# # 2. The Child Class (inherits everything from Animal)
# class Dog(Animal):
#     # This method is unique to Dogs
#     def bark(self):
#         print(f"{self.name} says Woof!")


# # 3. Another Child Class (inherits everything from Animal)
# class Cat(Animal):
#     # This method is unique to Cats
#     def meow(self):
#         print(f"{self.name} says Meow!")
# # Create instances of the child classes
# buddy = Dog("Buddy")
# whiskers = Cat("Whiskers")

# # 🔗 Using inherited methods (from Parent)
# buddy.eat()  # Outputs: Buddy is eating.
# whiskers.sleep()  # Outputs: Whiskers is sleeping.

# # 🎯 Using unique methods (from Child)
# buddy.bark()  # Outputs: Buddy says Woof!
# whiskers.meow()  # Outputs: Whiskers says Meow!

# # ❌ A Cat cannot bark, and a Dog cannot meow
# # whiskers.bark() -> This will throw an AttributeError












# # multi level inheritance
# # Tier 1: The Grandparent Class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def move(self):
#         print(f"This {self.brand} is moving forward.")


# # Tier 2: The Parent Class (Inherits from Vehicle)
# class Car(Vehicle):
#     def honk(self):
#         print(f"{self.brand} car goes Beep Beep!")


# # Tier 3: The Child Class (Inherits from Car)
# class ElectricCar(Car):
#     def charge(self):
#         print(f"Plugging in the {self.brand} to charge the battery.")
# # Create an instance of the bottom-tier class
# my_tesla = ElectricCar("Tesla")

# # 1. Accesses Tier 1 (Grandparent) method
# my_tesla.move()  # Outputs: This Tesla is moving forward.

# # 2. Accesses Tier 2 (Parent) method
# my_tesla.honk()  # Outputs: Tesla car goes Beep Beep!

# # 3. Accesses Tier 3 (Own) method
# my_tesla.charge()  # Outputs: Plugging in the Tesla to charge the battery.














# multiple 
# Parent Class 1
# class Camera:
#     def take_photo(self):
#         print("📸 Photo captured successfully!")


# # Parent Class 2
# class Phone:
#     def make_call(self, number):
#         print(f"📞 Dialing {number}...")


# # Child Class inheriting from BOTH Parents
# class Smartphone(Camera, Phone):
#     def browse_internet(self):
#         print("🌐 Loading web page...")
# my_phone = Smartphone()

# my_phone.make_call("555-0199")  # Inherited from Phone
# my_phone.take_photo()  # Inherited from Camera
# my_phone.browse_internet()  # Smartphone's own method











# hireachicaql
# The Shared Parent Class
# class SchoolMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hi, my name is {self.name} and I am {self.age} years old.")


# # Child Class 1 (Inherits from SchoolMember)
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)  # Initialize parent traits
#         self.salary = salary

#     def teach(self):
#         print(f"{self.name} is now teaching the class.")


# # Child Class 2 (Inherits from SchoolMember)
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)  # Initialize parent traits
#         self.marks = marks

#     def study(self):
#         print(f"{self.name} is now studying for exams.")
# # Create objects from different child classes
# prof_smith = Teacher("Mr. Smith", 42, 50000)
# alice = Student("Alice", 19, 92)

# # 🔗 Both access the shared parent functionality
# prof_smith.introduce()  # Outputs: Hi, my name is Mr. Smith and I am 42 years old.
# alice.introduce()  # Outputs: Hi, my name is Alice and I am 19 years old.

# # 🎯 Each accesses their own unique functionality
# prof_smith.teach()  # Outputs: Mr. Smith is now teaching the class.
# alice.study()  # Outputs: Alice is now studying for exams.

# # ❌ They cannot access each other's unique methods
# # alice.teach() -> Throws an AttributeError




# hybrid
# 1. Base Class (Grandparent)
# class Device:
#     def power_on(self):
#         print("🔌 Device powering up...")


# # 2. Hierarchical split from Device
# class Handheld(Device):
#     def check_battery(self):
#         print("🔋 Battery at 85%")


# class Phone(Device):
#     def dial_number(self):
#         print("📞 Connecting call...")


# # 3. Multiple inheritance merging both branches
# class Smartphone(Handheld, Phone):
#     def open_app(self):
#         print("📱 Opening app...")
# my_phone = Smartphone()

# my_phone.power_on()  # Triggers Grandparent (Device)
# my_phone.check_battery()  # Triggers Left Parent (Handheld)
# my_phone.dial_number()  # Triggers Right Parent (Phone)
# my_phone.open_app()  # Triggers its own unique behavior