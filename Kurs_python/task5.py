s = input()
n = 0
l = s[0]
for i in s:
    if l == i:
        n += 1
    else:
        print(l + str(n), end="")
        l = i
        n = 1
print(l + str(n))

