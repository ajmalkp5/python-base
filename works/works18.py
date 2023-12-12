# 1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers

# lst=[0,-1,-3,1,-10,12,4,6,8]

# for i in range(0,len(lst)-2):
#     for j in range(1,len(lst)-1):
#         for k in range(2,len(lst)):
#             if lst[i]+lst[j]+lst[k]==0:
#                 print(lst[i] , lst[j],lst[k] ,"\n")



#   2. Write a python program to make combinations of 3 digits

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))

# number=str(num1)+str(num2)+str(num3)
# print(f"number= {number}")




# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


for i in range(1, 6):
    for j in range(1,6-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(6-1,0, -1):
    for j in range(1,6-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()