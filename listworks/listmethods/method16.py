lst=["red","green","blue","white","black","apple","ignore","under"]
#q1 print words starting with vowels

vow_words=[w for w in lst if w[0] in ["a","e","i","o","u"]]
print(vow_words)

# q2 print words starting with consonants

con_words=[w for w in lst if w[0] not in ["a","e","i","o","u"]]
print(con_words)