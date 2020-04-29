num = int(input())
reklama = "... Читайте продолжение в источнике..."
c = '3'
while c != '.':
    c = input()
    if c == '.':
        break
    elif len(c) > num:
        test = c[:num]
        print(test + reklama)
    elif len(c) < num:
        print(c)
    else:
        continue

