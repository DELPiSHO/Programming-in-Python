n = input()
n = n.replace("\t"," ")
len1 = len(n)
len2 = 0
n = n.lstrip()
n = n.rstrip()
len2 = len(n)
suma = len1 - len2
print(n)
print(suma)