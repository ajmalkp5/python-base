#length = ascending order

text="good evening all"
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w),reverse=True)

print(srt_words)


# text="good evening all"
# words=text.split(" ")
# srt_words=sorted(words,key=lambda w:)

# print(srt_words)#all good evening