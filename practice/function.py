# positioned arg

# def func(a,b):
#     print(a+b)
#     return f"{a}+{b}={a+b}"
# print(func(10,20))


# keyword arg

# def func(a, b):
#     print(a + b)
#     return f"{a}+{b}={a + b}"
# print(func(a=10,b=20))


# mixed arg---> position aarg must be 1st in order

# def func(a, b):
#     print(a + b)
#     return f"{a}+{b}={a + b}"
# print(func(10,b=20))


# postion only arg---- must have '/' at the end of para 

# def func(a, b,/):
#     print(a + b)
#     return f"{a}+{b}={a + b}"
# print(func(10,20))


# keyword only arg--- must start with *
# def func(*,a, b):
#     print(a + b)
#     return f"{a}+{b}={a + b}"
# print(func(a=10,b=20))


# combination of keyword only and postion only----- must have '/' where we want postion arg
# def func(a, b,/,c):
#     print(a + b+c)
    
# print(func(10,20,c=10))



# default arg
# def func(a, b=2):
#     print(a + b)
#     return f"{a}+{b}={a + b}"
# print(func(10))


# positional arg packing (var len arg)---use '*' in para
# def func(*args):
#     print(*args,sep='\n')
# print(func(10,20,200,2089,329))




# keyword arg packing(var len arg )--- use '**' in para
# def func(**kwargs):
#     print(*kwargs,end='')

# print(func(a=10,b= 20,c= 200,d= 2089,e= 329))


# postional unpacking---use '*' in arg
# def func(a,b,c):
#     print(a,b,c)
# z=[1,2,3]
# print(func(*z))



# keyword unpacking ---- use '**' in arg, *,keynames in para
# def details(*,name,age):
#     print(name,age)
# d = {"name": "mgd", 'age': 22}
# details(**d)