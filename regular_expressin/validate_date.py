from re import *

date=input("enter a date ")

rule="(0[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(rule,date)

print("invalid" if matcher ==None else "valid")