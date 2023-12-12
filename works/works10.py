# 1. Write a Python program that ask users to enter a number and keep asking the users to enter a correct number, until the number with in the range that we given

# start_num=1
# end_num=10

# for i in range(3):
#     user_input=int(input(f"enter a number between {start_num} and {end_num}:"))
#     if start_num<=user_input<=end_num:
#         print(f"you have entered {user_input} which is given in range")
#         break
#     else:
#         print(f"number should be between {start_num} and {end_num}")




# 2.Write a python program to list the even numbers from the range that given by the user and delete the multiplication of 5 from the list

# user_input=int(input("enter the start number"))
# number=int(input("enter the end range"))

# for i in range(user_input,number):
#     if i %2==0 and i %5!=0:
#         print(i)

# 3.Pattern print 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *

# n=5
# for i in range(1,6):
#     for k in range(i,5):
#         print(" ",end="")
#     for w in range(0,i):
#         print("*",end=" ")
#     print()
# for i in range(1,6):
#     for k in range(i,1,-1):
#         print(" ",end="")
#     for w in range(6,i,-1):
#         print("*",end=" ")
#     print()