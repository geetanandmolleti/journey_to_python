# class Bawarchi:
#     menu = {
#         "starters": {
#             "chilli chicken": 260,
#             "chicken 65": 280,
#             "chicken lolipop": 240,
#             "prawns": 360,
#             "crispy corn": 180,
#             "majesticpaneer ": 240,
#             "mushroom crispy": 200,
#         },
#         "main course": {
#             "chicken biryani": 320,
#             "mutton biryani": 380,
#             "paneer butter masala": 260,
#             "kadai chicken": 290,
#             "dal tadka": 180,
#             "jeera rice": 150,
#             "butter naan": 45,
#             "garlic naan": 55,
#             "veg fried rice": 220,
#             "chicken noodles": 240,
#         },
#         "desserts": {
#             "gulab jamun": 90,
#             "rasmalai": 120,
#             "sizzling brownie": 180,
#             "vanilla ice cream": 80,
#             "fruit salad": 110,
#         },
#     }

#     def __init__(self):
#         self.cart = {}
#         self.total = 0
#     def add1(self,item,count=1):
#         if item in self.cart:
#             self.cart[item]+=count
#         for i in self.menu:
#             if item in self.menu[i]:
#                 self.cart[item]=count
#                 return 'added to cart'
#         return f'{item} is not avaliable'
        
#     def  display(self,val):
        

#         # for i in self.menu:
#                 # for j in (0,self.menu[i]):
#                 # print(self.menu[i].keys())
#         print(list(self.menu[val].keys()))
#     def remove_from_cart(self,item):
#         if item in self.cart.items(): 
#            self.cart.pop(item)
#         else:
#             print('no '+item+'in cart')
    
    
    
    
#     def bill(self):
#         self.total = 0  

#         for i, q in self.cart.items():
#             item_price = 0
#             for category in self.menu:
#                 if i in self.menu[category]:
#                     item_price = self.menu[category][i]
#                     break

#             item_total = item_price * q
#             self.total += item_total
#             print(item_total)

#         print("Grand Total:" + str(self.total) + '\n')
#         return self.total
#     def chef(self):
#         self.chef_cart={}
#         for i,j in self.cart.items():
#             if i not in self.chef_cart:
#                 self.chef_cart[i]=j
#         print(self.chef_cart)
            
        
        

# d1=Bawarchi()
# d1.add1("chicken biryani")
# d1.add1("chicken 65")
# d1.add1("crispy cor")
# print("cart is "+ str(d1.cart))
# d1.display("starters")
# d1.remove_from_cart("chicken biryani")
# d1.remove_from_cart("majesticpaneer")
# d1.bill()
# d1.chef()



# class Bank:
#     ceo = 'elon musk'
#     pin = '010403'
#     bal=0
#     set1=set()
#     @classmethod
#     def check(cls,val,new_ceo):
#         if val==Bank.pin:
#             cls.ceo=new_ceo
#         else:
#             print('invalid credentials')
            
#         print(Bank.ceo)
#     def user(self,amount):
#         if amount>0:
#             self.bal+=amount
#         elif amount<0:
#             self.bal+=amount
#         print(self.bal)
#     def register(self,name):
#         if name not in self.set1:
#             self.set1.add(name)
#             print('registered sucessfully')
#         else:
#             print('user alresy exists')
            
        
# o1=Bank()

# # registration
# user_name = input("enter user name.  ")
# o1.register(user_name)

# #ceo name to be changed
# after_name=input('please refer new ceo ')
# Bank.check('010403',after_name)

# #deposit and withdraw
# n = float(input("Enter deposit amount (positive) or withdraw amount (negative): "))
# o1.user(n)




# class bankacc:
#     def __init__(self, acc, bal, pin, age):
#         self.bal = bal
#         self.acc = acc
#         self.pin = pin
#         self.age = age


# class savings(bankacc):
#     def __init__(self, acc, bal, pin, age):
#         if bal<=500:
#             print('not sufficient fund')
#         else:
#             self.bal = bal
#         self.acc = acc
#         self.pin = pin
#         if age <= 21:
#             print("not suitable age")
#         else:
#             self.age = age

#     def deposit(self, amount):
#         if self.valid(amount):
#             self.bal += amount
#             print("deposited")
#         else:
#             print("not valid amount")

#     @staticmethod
#     def valid(a):
#         if type(a) in (int, float):
#             if a > 0:
#                 return True
#         return False


# obj1 = savings(121, 2234, 23, 223)
# print(obj1.age)






# class Bankacc:
#     b_name='sbi'
#     def __init__(self,acc,bal,pin):
#         self.acc=acc
#         self.bal=bal
#         self.pin=pin
# class savings(Bankacc):
#     def __init__(self, acc, bal, pin):
#         if bal>=1000:
#            super().__init__(acc, bal, pin)
#         else:
#             print('insufficient funds')
# class childsavings(savings):
#     def __init__(self, acc, bal, pin,age):
#         if age<21 and age>11:
#             super().__init__(acc, bal, pin)
#             self.age=age
#         else:
#             print('invalid age')
# # obj=Bankacc(234,1234,12)
# obj = childsavings(234, 1234, 12,15)
# print(obj.age)
# print()








# class CryptoWallet:
#     def make_payment(self, amount):
#         return f"Paid ${amount} using Bitcoin."


# class CreditCard:
#     def make_payment(self, amount):
#         return f"Paid ${amount} using Visa Corporate Card."


# def process_transaction(payment_gateway, amount):
#     print(payment_gateway.make_payment(amount))


# crypto = CryptoWallet()
# card = CreditCard()

# process_transaction(crypto, 250)
# process_transaction(card, 1200)
# print(1780748811.527703-1780748811.527689)