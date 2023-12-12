expenses=[1200,1222,7777,5555,87543,23373,11222,2112,21122,]

# find costly value

max_exp=max(expenses)
print(max_exp)

# another way of finding method

max_exp=max(expenses)
print(f"maximum={max_exp}")


#minimum
min_exp=min(expenses)
print(min_exp)

# another way of finding method

min_exp=min(expenses)
print(f"minimum={min_exp}")

#total expense

tot_exp=sum(expenses)
print(tot_exp)

# another way of finding method

tot_exp=sum(expenses)
print(f"total={tot_exp}")

#average expense

avg_exp=tot_exp/len(expenses)
print(avg_exp)
print(f"average={avg_exp}")