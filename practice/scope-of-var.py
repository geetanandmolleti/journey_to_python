# global variable a 
# def func():
#     print(a)
# a=10 
# print(func())



# local variable a 
# def func():
    # a=10
    # print(a)
# #print(a) #--here a cant be accessed
# print(func())


# here a is enclosed variable
# def func():
#     a=10
#     def func1():
#         b=11
#         print(a,b)
#     func1()
# print(func())



# use of global keyword


# a=10
# def add():
    # global a
#     a=11
#     print(a)
# add()
# print(a)



# use of nonlocal keyword
# def outer_func():
#     a = 10  # A local variable to outer_func, but nonlocal to inner_func

#     def inner_func():
#         nonlocal a  # Targets the variable in outer_func
#         a = 11
#         print(a)

#     inner_func()
#     print(a)


# outer_func()



