from re import *

text="aaabaabcaaabvaaaam"
# pattern="a*"  # any number of a including zero numbers [a-z]*
# pattern="a{2}"  # a{2}= how many times of a
pattern="a{2,4}"  #a{2,4}=2 to 4 number hoew many time

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())
    