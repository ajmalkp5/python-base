# 1. Write a Python program that keep on accepting number from the user until users enter zero display the sum of all number

use_inp=int(input(""))

# 2.Write a python program to accept decimal number and display it’s binary number

num=int(input("enter the number"))
org_num=num
binary=""
if num==0:
    binary=0
else:
    while num>0:
        digit=num%2
        binary=str(digit)+binary
        num=num//2
print(f"the binary of {org_num} is {binary}")


# 3.Pattern print 
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

# for row in rin range(1,row+1):
#         print(row,end=" ")
    # print()ange(6,0,-1):
    # for col 