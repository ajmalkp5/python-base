from re import *

text="advbhfsAscsa238430.;'.[]*&*^cee"

# pattern="[ac]"  #[] bracket define or eg ac= a or c
# pattern="[a-e]" # chck all alphabet character a to e
# pattern="[a-z]" #[a-z]lower case of all aphabets
# pattern="[A-Z]" #[A-z]upper case of all alphabets
# pattern="[a-zA-Z]" #[a-zA-Z]matches all alphabets
# pattern="[0-9]" #check for all digits
# pattern="[a-zA-Z0-9]" #alphanumeric charecters checking
# pattern="[^a-z]" #exclude a-z
pattern="[^a-zA-Z0-9]" #for special characters

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())