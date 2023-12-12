# sqauare of list element

lst=[2,4,3,5,6,7]
sqaures=[]

for num in lst:
    sq=num**2
    sqaures.append(sq)

print(sqaures)

# even or odd
evens=[]
for num in lst:
    if num%2==0:
        evens.append(num)
print(evens)
