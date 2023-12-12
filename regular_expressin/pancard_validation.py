from re import *

pan_number=input("enter a pan number:")

rule="[A-Z]{3}[PACFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(rule,pan_number)

print("valid" if matcher !=None else "invalid")