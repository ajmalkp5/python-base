# validate year 1900-2024

from re import *

year=input("enter a year")

rule="(19|20)[0-9]{2}"

matcher=fullmatch(rule,year)

print("invalid" if matcher ==None else "valid")