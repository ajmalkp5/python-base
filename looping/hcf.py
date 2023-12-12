num1=int(input("enter a number"))
num2=int(input("enter a number"))
smallest_num=num1 if num1<num2 else num2
fact=1
i=1
while(i<=smallest_num):
    if(num1%i==0 and num2%i==0):
        fact=i
    i+=1

print(fact)        
