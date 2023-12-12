from re import *

f=open("C:\\Users\\ASUS\\Desktop\\my python\\regular_expressin\\vehicle_num.txt","r")

rule="(KL|TN)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher !=None:
        print(number)