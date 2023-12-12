# text="hello hai hello hai"
# word count

text="hello hai hello hai"

words=text.split(" ")
word_count={}

for wc in words:
    if wc in word_count:
        word_count[wc]+=1
    else:
        word_count[wc]=1
print(word_count)