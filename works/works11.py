# 1. Write a Python program that print 2 list and common element

# fst=[2,4,6,8,10,12,14,]
# scnd=[1,3,5,6,7,4,2,8,5]
# c_list=[]
# for num in fst:
#     if num in scnd:
#         c_list.append(num)
# print(fst)
# print(scnd)
# print(c_list)


# 2.Write a python program to find the least square number from a list

fst=[2,4,5,7,8,10]
sq_lst=[num**2 for num in fst]
least_sq=min(sq_lst,key=lambda x:(x-round(x**0.5)**2))
print(sq_lst)
print(least_sq)


# 3.Pattern print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end="\t")
#     print()