# 1. Write a Python program to find n natural number in ascending order

# n=int(input("enter the number"))
# for i in range(0,n+1):
#     print(i)


# # 2.Write a python program to find n natural number in descending order

# n=int(input("enter a number"))
# for i in range(n,-1,-1):
#     print(i)


# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

for i in range(1,6):
    for k in range(i,5):
        print(" ",end=" ")
    for n in range(0,i):
        print("*",end=" ")
    print()