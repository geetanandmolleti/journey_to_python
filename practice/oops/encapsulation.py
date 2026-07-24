# the hiding using --->'__'
# class PiggyBank:
#     def __init__(self):
#         self.__money = 0  # The '__' hides it from the outside world


# box = PiggyBank()

# # This crashes! Python prevents you from touching the hidden money.
# print(box.__money)











# getter and setter part 
# class Thermostat:
#     def __init__(self, temp):
#         self.__temp = temp

#     @property
#     def temp(self):  # The Getter
#         return self.__temp

#     @temp.setter
#     def temp(self, new_temp):  # The Setter
#         if new_temp < -273:
#             print("Error: Impossible temp!")
#         else:
#             self.__temp = new_temp


# # Test it out
# house = Thermostat(20)

# house.temp = 25  # Looks like normal variable access, but runs the setter!
# print(house.temp)  # Looks like normal variable access, but runs the getter!