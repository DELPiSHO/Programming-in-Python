l=[i for i in iter(input,'.')]
w='python'
k=0
for j in l:
    if w in j.lower().split():
        k+=1
print (*[j[k-1] for j in l if k>0])