# simple way or shortcut

from re import *

text="ab caK7@%"
# # pattern="\d"  #\d=[0-9]
# pattern="\D"  #\D=[^0-9]
# pattern="\w"  #\w=alphanumeric character "[a-zA-Z0-9]"
pattern="\W"  #\w=special charcters "[^a-zA-Z0-9]"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())