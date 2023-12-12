num=input("enter a number")
digit_count=len(num)
num=int(num)
original=num
sum=0

while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10

print(f"{original} is a armstrong number" if original==sum else "not armstrong number")
