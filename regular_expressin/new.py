# question
# starting with k,l,m,n
# second place must be a digit and that is divisible by 3
# followed by any number of alphsabets and numbers


# k5abc

from re import *

variable_name=input("enter a variable")

rule="[k-nK-N][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid" )