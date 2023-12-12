# 1. Write a Python program that Use while loop to display elements from a given list present at odd index positions


# fst=[20,40,55,12,82,6,75,78,54,34]
# index=1
# while index <len(fst):
#     print(f"elements of i {index} is {fst[index]}")
#     index+=2


# 2.Write a python program that Take input from user and make square list of the number and the cube list .Range is 10 number in the list

# num=int(input("enter a number:"))
# sqr=[i ** 2 for i in range(num,num+10)]
# cube=[i ** 3 for i in range(num,num+10)]
# print(f"square:{sqr}")
# print(f"cube:{cube}")


# 3.Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

# rows=5
# for i in range(1,rows,+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()