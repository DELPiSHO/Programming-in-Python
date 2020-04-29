list = []
c = '3'
while c != '.':
    c = input()
    if c == '.':
        break
    elif int(c) % 2 == 0:
        list.append(c)
    else:
        continue
list.reverse()
list = ' '.join(list)
print(list)