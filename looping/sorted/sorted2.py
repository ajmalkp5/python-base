#find it is an anagram word

source_word="won"

target_word="now"

srt_swd=sorted(source_word)
srt_tgwd=sorted(target_word)

print("True" if srt_swd==srt_tgwd else "False")

