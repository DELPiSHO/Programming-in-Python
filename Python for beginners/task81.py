n = [i for i in input()]
text = []
new = []
suma = 0
for i in n:
    if i.isdigit():
        i = int(i) + 1
        text.append(i)
    else:
        text.append(i)
for i in text:
    if i == 10:
        i = 0
    new.append(i)
new = ''.join(str(i) for i in new)
print(new)
for i in new:
    if i.isdigit():
        suma = suma + int(i)
print(suma)