from re import *

mob_num=input("enter a number")

rule="([+]91)?[0-9]{10}"

matcher=fullmatch(rule,mob_num)

print("invalid" if matcher ==None else "valid")