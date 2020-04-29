import re

text = []
helper = []
while True:
    i = input()
    if i == '.':
        break
    else:
        if 'POST' in i:
            i = i.replace('POST ','')
            text.append(i)
        if 'GET' in i:
            print(text[-1])
        if 'DELETE' in i:
            del text[-1]
print(*text)
