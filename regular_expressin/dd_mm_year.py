from re import *

full_date=input("enter a date ")

rule="(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-(19|20)[0-9]{2}"

matcher=fullmatch(rule,full_date)

print("invalid" if matcher ==None else "valid")