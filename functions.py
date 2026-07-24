# matrix addition via validation


# m=[[1,2,3],
#    [4,5],
#    [7,8,9]]
# n=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# if len(m)!=len(n):
#   print('cannot')
# count1,count2=0,0
# for i in range(len(m)):
#   for j in range(len(m[i])):
#     count1+=1
# for i in range(len(n)):
#   for j in range(len(n[i])):
#     count2+=1
# if count1!=count2:
#    print('cannot be added')
#    val=False

# m1=max(len(m),len(n))
# res=[]
# if val!=False:
#    for i in range(len(m[0])):
#       res.append([])
#       for j in range(len(m[i])):
#          x=m[i][j]+n[i][j]
#          res[i].append(x)
# print(res)
# res2=[]
# for i in range(len(res[1])):
#   res2.append([])
#   for j in range(len(res)):
#     res2[i].append(res[j][i])


# str11='this is a string'.split(" ")
# seen={}
# for i in str11:
#   if i in seen:
#     seen[i]+=1
#   else:
#     seen[i]=1
# print(seen)


# print(dir(list))
# m = [[1, 2, 3], [4, 5], [7, 8, 9], [0]]
# print(len(m[1]))




#to check even length string in list
# # int1 = input("enter here ")
# int2 = int1.split(" ")


# def check(a):
#     for i in range(len(a)):
#         if len(a[i]) % 2 != 0:
#             return False
#     return True


# a = check(int2)

# print(a)


# #frequency of words in a sentence
# str1=input('enter the sentence').split(' ')
# seen={}
# for i in str1:
#     if i in seen:
#         seen[i]+=1
#     else:
#         seen[i]=1
# print(seen)




#anagram

# str1 = input("enter the characters sepearsted by space ").split(" ")
# seen = []


# def group_anagrams(x):
#     sorted_word = "".join(sorted(x))

#     if sorted_word not in seen:
#         seen.append(sorted_word)


# for i in range(len(str1)):
#     a = group_anagrams(str1[i])

# print(seen)




#longest substring
# str1 = input("enter the sentence ")
# prev = -1
# val1 = "" 


# def longest(val):
#     global val1, prev

#     if val in str1 + str1 and len(val) > prev:
#         val1 = val
#         prev = len(val1)


# for i in range(len(str1)):
#     for j in range(i + 1, len(str1)):
#         if len(set(str1[i : j + 1])) == len(str1[i : j + 1]):
#             longest(str1[i : j + 1])

# print("Longest unique substring:", val1)





# #peak element finder
# print('enter ypur list')
# list1=list(map(int, input().split(',')))
# def peak(lst):
#     for i in range(3,len(lst)):
#         if lst[i-2]>lst[i-1] and lst[i-2]>lst[i-3]:
#             return lst[i-2],i-2
# c=peak(list1)
# print(c)




#tensar validation 
# n= input('enter number of rows')

# res=[]
# for i in range(int(n)):
#     res.append(input('enter values sepearated by space').split(' '))
# print(res)
# def check(list1):
#     for i in range(len(list1)):
#         if len(list1[0])!=len(list1[i]):
#             return False
#         for j in range(len(list1[i])):
#             if type(list1[i][j]) != type(list1[0][0]):
#                 return False 
# a=check(res)
# print(a)



#doubt
# def  isprime(n):
#     if n==1:
#         return False
#     for i in range(2,int(n**0.5)):
#         if n%i==0:
#             return False
#     return True
# n=8
# c=1

# for i in range(n):
#     c2=0
#     l=[]
#     while c2<=i:
#         if not isprime(c):
#             l.append(str(c))
#             c2+=1
#         c+=1
#     if i%2==0:
#         print(*l[::-1])
#     else:
#         print(*l)








#wap to print divisor of  number  which is divisble by any prime between 1 and that number


# n1=int(input('enter the number '))
# list1=[]
# def check(val):
#     for i in range(2,int(val**0.5)+1):
#         if val%i==0:
#             return False
#     return True
# for i in range(2,n1):
#     if  check(i)==True and n1%i==0:
#         list1.append(i)
        
# if len(list1)==0:
#     print(' no prime divisibles')
# else:
#     print([i for i in list1])       
        





# #wap to generate sequential 2d matrix
# r=int(input('enter number of rows '))
# c=int(input('enter number of columns '))
# list1=[]


# def generate(r1,c1):
#     count = 0
#     for i in range(r):
#        list1.append([])
#        for j in range(c):
#            count+=1
#            list1[i].append(count)
#     print(list1)
# print(generate(r,c))


##restricting for non int
# def func(*args):
#     for i in args:
#        if type(i)!=int:
#            return 'cannot'
# n1=eval(input("enter  values with ,"))
# # print(func(10,20,'hello'))
# print(func(n1))





#to print keys in dict from keyword paramaters packing
# def func(**kwargs):
#     for i in kwargs:
#         print(kwargs[i])
# x=func(name='geetanand', stream='python')
# print(x)




# #calculator problem
# def func(operand, *args):
#     val = 0
#     val1 = 1

#     if operand == "addition":
#         for i in args:
#             val += i

#     if operand == "multiplication":
#         for i in args:
#             if i == 0:
#                 continue
#             val1 *= i

#     return val, val1


# val, val1 = func("multiplication", 10, 20, 30, 40, 50,54,65,765,765,44,54,432)

# if val == 0:
#     print(val1)
# else:
#     print(val)







# #template engine
# def template_engine(**kwargs):
#     str1='<a '+str(kwargs)
#     # for i in kwargs:
#     #     str1+=str(kwargs)
#     #     # str1+=kwargs[i]
#     #     # str1+=' '
#     str1+='> </ a>'
#     print(str1)
#     str2=''
#     for i in str1:
#         if i=="{" or '}':
#             continue
#         else:
#             str2+=i
#     print(str2)


# a = template_engine(href="path", target="_self_")



# def calci(lst):
#     operator = lst[0]
#     numbers = lst[1:]

#     result = numbers[0]
#     for num in numbers[1:]:
#         result = eval(f"{result} {operator} {num}")

#     return result


# n1 = input("enter operator and values with spaces: ")
# list1 = list(map(lambda x: int(x) if x.isdigit() else x, n1.split(" ")))
# print(calci(list1))



# def gcd(a,b):
#     x=min(a, b)
#     for i in range(x,2,-1):
#         if a%i==0 and b%i==0:
#             return i
#     # i=2
    
#     # while i<=(a-b):
#     #     if a%i==0 and b%i==0:
#     #         res=i
#     #     i+=1
#     # print(res,i)
# res = 0
# print(gcd(12,6))




# import math
# def lcm(a, b):
#     x = max(a, b)
#     for i in range(2,x**5):
#         if i%a == 0 and i%b == 0:
#             return i






# def lcm(a, b):
#     n=a*b
#     res=0
#     while n>2:
#         if n%a==0 and n%b==0:
#             res=n
#         n-=1
#     print(res)
# print(lcm(15,16))

# print(math.lcm(15,16))





# def strong(x):
#     x2=x
    
#     res=0
#     while x2>0:
#         fact = 1
#         digit=x2%10
        
#         while digit>0:
#             fact*=digit
#             digit-=1
#         res += fact
#         x2=x2//10
       
#     if res==x:
#        print('true')
#     else:
#        print(res)
# a=strong(145)






# def strong(x):
#     temp = x
#     memo = {}
#     total = 0

#     while temp > 0:
#         digit = temp % 10

#         if digit in memo:
#             fact = memo[digit]
#         else:
#             fact = 1
#             for i in range(1, digit + 1):
#                 fact *= i
#             memo[digit] = fact

#         total += fact
#         temp //= 10

#     if total == x:
#         print(total, memo)
#     else:
#         print(total,memo)


# strong(1453)


# list1=[1,2,[1,2],[[[1,2,3]]]]
# print(len(list1))
# res=[]
# for j in range(len(list1)):
#     if type(list1[j])!=list:
#         continue
#     else:
#        for i in range(len(list1[j])):
#           if type(list1[i])!=list:
#               res.append
# (list1[i])
    
# print(res)







# def lst(list1):
#     for i in range(list1):
#         if type(list1[i])==list:
#             lst(list1[i])
#         else:
#             res.append(list1[i])
# for i in range(len(list1)):
#     if type(list1[i])==list1:
#         lst(list1[i])
#     else:
#         res.append(list1[i])
# print(res)






# list1 = [1, 2, [1, 2], [[[[[[[[[[[[1, 6]]]]]]]]]]]], [[[1, 2, 3]]]]


# def flat(nested_list):
#     res = [] 

#     i = len(nested_list)
#     while i > 0:
#         item = nested_list[i - 1]
#         if type(item) != list:
#             res.append(item)
#         else:
#             res.extend(flat(item))
#         i -= 1

#     return res  


# final_result = flat(list1)
# print(final_result[::-1])






#reverse string usingion
# def rev(str1):
#     if len(str1)<=1:
#         return str1
#     return str1[-1]+rev(str1[:-1])
# str1='hello'
# print(rev(str1))



# count using recursion
# val=1
# def count(x):
#     if x<=1:
#         return x
#     global val
    
#     x=x//10
#     val += 1
#     return count(x)
# print(count(9))
# print(val)






#sum using recursion

# list1=[1,5,7,7,90]
# res=0
# def add(list1):
#     global res
#     if len(list1)<=0:
#         return res 
#     res+=list1[0]
#     return add(list1[1:])
# print(add(list1))


# deep count using recursion
# list1 = [1, 2, 3, [2, 4, [[[12, 35, 67, 65]]]]]
# def deepcount(lst):
#     count=0

#     for i in range(len(lst)):

#         if type(lst[i])!=list:
#              count += 1
#         if type(lst[i])==list:

#             count+= deepcount(lst[i])
#     return count
# print(deepcount(list1))


# creating 5 users

# def create(*args):
#     seen=[]
#     for i in args:
#         if i in seen:
#             print('cannot generate')
#         else:
#             seen.append(i)
# for i in range(5):
#     inp = input("enter ").split(",")
#     print(create(inp))




# int to bin without function
# n=11

# n1=n
# def bina(n1):
#     str1 = ""
#     for i in range(2,n1):
#        str1+= str(n1%2)
#        n1=n1//2
#     print(str1)
# print(bina(n1))





# maximum sum row in list
# list1=[[1,2,3],[4,5,6],[65,87,9]]
# def check(list1):
#     maxi=0
#     maxo=0
#     for i in range(len(list1)):
#         summ=0
#         for j in range(len(list1[i])):
#             summ+=list1[i][j]
#         if summ > maxi:
#             maxi = summ
#             maxo = i
            
        
#     print(maxi,maxo)
# print(check(list1))





# # adding 2 matrices in better way
# m=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# n=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]


# def check(m,n):
#     res=[]        
#     for i in range(len(m)):
#         if len(m[i])!=len(m[0]) or len(n[i])!=len(n[0]):
#            print('cannot be added')
#         res.append([])
#         for j in range(len(m[i])):
#             res[i].append(m[i][j]+n[i][j])
#     print(res)
# print(check(m,n))



# sudoku
# def sudoku(board):
#     for r in range(9):
#         if len(set(board[r])) != 9:
#             return False

#     for c in range(9):
#         column = []
#         for r in range(9):
#             column.append(board[r][c])
#         if len(set(column)) != 9:
#             return False

#     for r_start in (0, 3, 6):
#         for c_start in (0, 3, 6):
#             lst = []
#             for i in range(3):
#                 for j in range(3):
#                     lst.append(board[r_start + i][c_start + j])
#             if len(set(lst)) != 9:
#                 return False

#     return True


# # matrix = [
# #     ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
# #     ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
# #     ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
# #     ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
# #     ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
# #     ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
# #     ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
# #     ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
# #     ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
# # ]


# matrix = [
#     [5, 3, 4, 6, 7, 8, 1, 9, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 9, 7, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 7, 1, 9],
# ]

# print(sudoku(matrix))
