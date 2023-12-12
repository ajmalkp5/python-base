from re import *

f=open("C:\\Users\\ASUS\\Desktop\\my python\\regular_expressin\\train.txt")

rule="[0-9]{5}"

for line in f:
    words=line.rstrip("\n")
    matcher=finditer(rule,words)
    for m in matcher:
        print(m.group())