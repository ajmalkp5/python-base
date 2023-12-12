dengue_list=("ekm","tsr","ekm","tvm","ekm","tvm","pkd","tvm","pkd","tvm")

wc={}

for dist in dengue_list:
    if dist in wc:
        wc[dist]+=1
    else:
        wc[dist]=1
print(wc)

srt_wc=sorted(wc,key=lambda k:wc.get(k),reverse=True)
print(srt_wc)