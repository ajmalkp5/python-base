num1=int(input("enter a number"))
num2=int(input("enter a number"))
smallest_num=num1 if num1<num2 else num2
hcf=1
i=1
while(i<=smallest_num):
    if(num1%i==0 and num2%i==0):
        hcf=i
    i+=1

print(f"hcf of {num1},{num2} = {hcf}")
lcm=(num1*num2)/hcf        
print(f"lcm of {num1},{num2} = {lcm}")
