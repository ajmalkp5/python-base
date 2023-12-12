expenses=[1200,1222,7777,5555,87543,23373,11222,2112,21122,]

# print all expenses > 3000

# for i in range(0,len(expenses)):
#     if expenses[i]>3000:
#         print(expenses[i])

# print all expense in range of 15k-25k
# easy
for i in range(0,len(expenses)):
        if expenses[i] in range(15000,25000):
                print(expenses[i])
# tough                # 
    # if expenses[i]>15000 and expenses[i]<25000:
        # print(expenses[i])