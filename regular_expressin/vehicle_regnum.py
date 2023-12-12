# kerala vehicle numbers
from re import *

vehicle_number=input("enter a VEHICLE NUMBER:")

# start with kl
# 2digit
# 2 alphabets
# 4 digit

rule="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(rule,vehicle_number)

print("invalid" if matcher==None else "valid")