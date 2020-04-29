b=[".", ",", "!", "?", ":", ";", "–"]
a=input().lower()
for n in b:
    a=a.replace(n,'')
print(a)
