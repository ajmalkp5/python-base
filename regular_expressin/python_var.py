
from re import *

variable_name=input("enter a variable")

rule="[a-zA-Z]{1}[a-zA-Z0-9_]*"

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid" )