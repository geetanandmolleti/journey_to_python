# abs without abs
# a=lambda a1: a1 if a1>0 else -a1
# print(a(0))

# max of 2 numbers
# a = lambda a1, a2: a1 if a1 > a2 else a2
# print(a(10, 20))


# lists into dict
# a = ["user", "password"]
# b = ["asp", "123"]
# val = map(lambda x, y: (x, y), a, b)
# print(dict(val))


# elements greater than avg of list
# a=[1,2,3,4,22,10]
# val= filter(lambda x: x>=sum(a)/len(a) ,a)
# print(list(val))


# # filter non empty string
# a=['cvhj','',' ']
# val=filter(lambda x: len(x)!=0,a)
# print(list(val))

# a = [12, "str", 12, "ed"]
# def check_int(item):
#     return type(item) is int
# val = filter(check_int, a)
# print(list(val))


# comprehension
# a=[i for i in range(1,50,2)]
# print(a)


# str1='XCFGHJKJHBV'
# a=[i.lower() for i in str1]
# print(a)


# a = [i for i in range(0, 50, 3)]
# print(a)


# a = [i for i in [10, 2, 5, 78, 9, 90] if i > 10]
# print(a)


# tup =[12,13,15,17,19,23,1,2,41,342]

# # a= [i for i in tup if i!= [j for j in range(2,i) if i%j==0]]
# # print(a)

# a=['pass' if i>=40 else 'fail' for i in tup]
# print(a)


# lst=[]
# tup = [[12, 13, 15],[ 17, 19, 23],[ 2, 41, 342]]
# a=[tup[i][j] for i in range(3) for j in range(3)]
# print(a)


# tup = [12, 13, 15, 17, ]
# a=[i if i%j==0 else None  for i in tup for j in range(2,i+1)]
# print(a)


# tup =[12, 13, 15, 17, ]
# a=[i  for i in tup for j in range(2,i+1)  if i%j!=0 ]
# print(a)

# print(a)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j]=a[j][i]
# print(val)


# a=[1,2,4,9]
# b=[3,8,9]
# val={a[i]:b[i] for i in range(min(len(a),len(b)))}
# print(val)

# a=[1,2,4,9]
# val= { a[k]:'even' if k%2==0 else 'odd' for k in range(len(a))}
# print(val)


# val={{i:'prime' for j in range(2,i) if not i%j} for i in range(10)}
# print(val)


# # decorators
# def first(para):
#     def wrapper():
#         return para()
#     return wrapper


# @first
# def starter():
#     return 'start'
# @first
# def ender():
#     return 'end'

# print(starter(),ender())


# # import time
# # def first(para):


# #     def wrapper():
# #         start=time.time()
# #         print(para())
# #         end=time.time()
# #         print(start, end)
# #         print(end - start)

# #     def wrapper2():
# #         return para
# #     return wrapper


# # @first
# # def starter():

# #     return 'start'
# # @first
# # def ender():
# #     return 'end'

# # print(starter())


# def wrapper(*args):
#     flag = True
#     for i in args:
#         if type(i) != t:
#             flag = False
#     if flag == True:
#         func(*args)
#     else:
#         print("type issue")





# lst=['geet','anand']

# def inner(func):
#     def wrapper(*args):
#         flag=True
#         for i in args:
#             print(i)
#             if i not in lst:
#                 flag=False
#         if flag:
#             func(*args)
#             print('authentication successful')
#         else:
#             print('unauthentication')
#     return wrapper



# @inner
# def add(a,b):
#     return 'checiking'
# add("geet", "1anand")
 







# lst=['geet','anand']
# def valid(t,t1):
#     def inner(func):
#         def wrapper(*args):
#             flag=True
            
#             if t not in lst or t1 not in lst:
#                 flag=False
#             if flag:
#                func(*args)
#                print('authentication successful')
#             else:
#                print('unauthentication')
#         return wrapper
#     return inner

# @valid("geet", "anand")
# def add(a,b):
#     return 'checiking'
# add(10,20)







# lst=['geet','anand']
# def valid(t,t1):
#     def inner(func):
#         def wrapper():
#             flag=True

#             if t not in lst or t1 not in lst:
#                 flag=False
#             if flag:
#                func()
#                print('authentication successful')
#             else:
#                print('unauthentication')
#         return wrapper
#     return inner

# @valid("geet", "anand")
# def add():
#     return 'checiking'
# add()


def valid(expected_rows, expected_cols):
    def inner(func):
        def wrapper(*args):
            for matrix in args:
                if len(matrix) != expected_rows:
                    return "invalid matrix: wrong row count"

                for row in matrix:
                    if len(row) != expected_cols:
                        return "invalid matrix: wrong column count"

            return func(*args)

        return wrapper

    return inner


@valid(3, 3)
def add(inp, inp2):
    res = []  
    for i in range(len(inp)):
        res.append([])
        for j in range(len(inp[i])):
            res[i].append(inp[i][j] + inp2[i][j])
    return res


matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(add(matrix_a, matrix_b))