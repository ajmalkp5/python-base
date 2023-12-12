# 1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

# num_grps = {}
# ognl_list = [1, 3, 5, 1, 3, 4, 6, 4, 2]
 
# for num in ognl_list:
#     if num not in num_grps:
#         num_grps[num] = [num]
#     else:
#         num_grps[num].append(num)

# result = list(num_grps.values())
# result.sort()
# print(result)



#2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000



unit=int(input("enter unit consumed "))

if unit<=100:
    print("bill amount is 0 ")
elif unit<=200:
    slab_1=unit-100
    bill=slab_1*5
    print(f"bill amount is {bill}")
elif unit>200:
    slab_2=unit-200
    bill1=slab_2*10
    slab_1=unit-(slab_2+100)
    bill2=slab_1*5
    print(f"bill amount is {bill1+bill2}")




# 3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E


# i=64
# for row in range(1,6):

#     for col1 in range(1, 6 - row):
#         print("",end=" ")
#     for col2 in range(1, row + 1):
#         print(chr(i+ col2),end=" ")
#     print()