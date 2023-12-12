# print all odd numbers from 20 to 100

i=1

end=int(input("enter limit"))

while(i<=end):
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i+=1        
