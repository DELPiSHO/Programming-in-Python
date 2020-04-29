a = 'test'
lol = []
while a.isupper() == False or a.islower() == False or a.isdigit() == False:
    a = input()
    if (a.isupper() == True or a.islower() == True or a.isdigit()):
        break
    elif a.isdigit() == False:
        lol.append(a)
    else:
        continue
for i in lol:
    odp = ''.join(c.lower() if c.isupper() else c.upper() for c in i)
    print(odp)