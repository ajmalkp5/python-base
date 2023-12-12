# find longest word from the list

items=["bat","arc","ball","stumps","cricket"]


# already set in alphabtic order 
longest_word=max(items)
print(longest_word)

# maximum word in charcter
longest_word=max(items,key=lambda w:len(w))
print(longest_word)

# minimum word in charcter

min_word=min(items,key=lambda w:len(w))
print(min_word)
 
# already set in alphabtic order 
min_word=min(items)
print(min_word)

# maximum word in character difficult
max_word=items[0]
for i in range(1,len(items)):
    current_word=items[i]
    if len(current_word)>len(max_word):
        max_word=current_word

print(max_word)


# # minimum word in character difficult

min_word=items[0]
for i in range(1,len(items)):
    current_word_word=items[i]
    if len(current_word)<len(min_word):
        min_word=current_word

print(min_word)
# sum word in character difficult
sum=0
for i in range(0,len(items)):
    current_word_word=items[i]
    sum=sum+len(current_word)
    min_word=current_word

print(f"total={sum}")