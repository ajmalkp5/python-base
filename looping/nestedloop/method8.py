text="sdhsGaeiuoaeiouDJHgvdhgvjGSDAHJFVGVshdabavchgJBAdhvb"

c_count=0

for ch in text:
    if ch not in ["a","e","i","o","u"]:
        c_count+=1
print(f"consonants count={c_count}")
print(f"total number of characters{len(text)}")

# right rule

text="23#4q24@sdhsGaeiuoaeiouDJHgvdhgvjGSDAHJFVGVshdabavchgJBAdhvb"

c_count=0

for ch in text:
    if ch not in ["a","e","i","o","u"]:
        if ch.isalpha():
            c_count+=1
print(f"consonants count={c_count}")
print(f"total number of characters{len(text)}")