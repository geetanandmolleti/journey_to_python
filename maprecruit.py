# 1st question


# nums=[1,2,0]
# nums=[3,4,-1,1]
# nums=[7,8,9,11,12]
# nums = [-1]
# i=1
# while i<=len(nums)+1:
#     if i in nums:
#         print("")
#     else:
#         val=i
#         print(i)
#         break
#     i=i+1
# # print(i)











# 2nd question

# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# # nums=[1]
# # k=1
# i = 0
# lst = []
# while i <= len(nums) - 3:
#     lst.append(nums[i : i + k])

#     i += 1
# a = []
# res = []
# for i in lst:
#     a = max(i)
#     res.append(a)
# if len(res)==0:
#     print(nums)
# if len(res)>0:
#     print(res)


    
    

# 3rd question
# nums=[5,2]
# # nums=[-1]

# res=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]:
#             res.append(nums[j])
#             break
# res.append(0)
# print(res)







# 4th question
# nums=[[9,9,4],[6,6,8],[2,1,1]]
# nums = [[3, 4, 5], [3, 2, 6], [2, 1, 1]]
# count = 0
# lst = []
# for i in range(len(nums) - 1):
#     for j in range(len(nums[i]) - 1):
#         lst.append((nums[i][j], nums[i + 1][j], nums[i][j + 1]))
# for i in range(len(lst) - 1):
#     for j in range(i + 1, len(lst) - 2):
#         if lst[i][j + 1] > lst[i][j]:
#             count += 2
#         if lst[i][j + 1] in lst[i + 1]:
#             count += 2
# print(count)
# print(lst)







# 5th question
# nums=[1,3,2,3,1]
# nums=[2,4,3,5,1]
# res=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]*2:
#             res.append(i)
#             res.append(j)
# print(len(res)/2)














# # 6th question
# n='123'
# n='1'
# for i in range(int(n)-1,-1,-1):
#     i=str(i)
#     if i==i[::-1]:
#         print(i)
#         break






































#extra

# nums=[1,3,-1,-3,5,3,6,7]
# k=3
# i=0
# lst=[]
# while i<=len(nums)-3:
#     lst.append(nums[i:i+k])
    
#     i+=1
# a=[]
# res=[]
# for i in lst:
#     a=max(i)
#     res.append(a)
# print(res)











# nums = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# # nums = [[3, 4, 5], [3, 2, 6], [2, 1, 1]]
# count = 0
# lst = []

# print(count)







# a=[[1,2,3],[8,9,4],[7,6,5]]
# m=len(a)
# n=len(a[0])
# res=[]
# for i in range(len(a)):
#     res=res+a[i]

# res=sorted(res)
# print(res)
# aa=[]
# for i in range(0,len(a),n):
#     aa.append(a[i:i+n])
# print(aa)








d = {}
s = "geetanand"
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)



class Maprecruit:
   
    
    def add_and_update(s):
        d={}
        s='geetanand'
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return d
    # def del():
    #     for i in s:
    #         if i in d:
    #             d[i]=0
x=Maprecruit()
print(x.add_and_update())