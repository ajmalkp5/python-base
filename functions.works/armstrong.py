def is_armstrong(num):

    digit_count=len(num)
    num=int(num)
    original=num
    sum=0
    while(num!=0):
        last_digit=num %10
        pow=last_digit**digit_count
        sum=sum+pow
        num=num//10
    return(True if sum==original else False)

print(is_armstrong("153")) 