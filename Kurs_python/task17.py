dict = {}
help = []
n = int(input())
for i in range(n):
    x = int(input())
    help.append(x)
for j in range(0,len(help)):
    key = help[j]
    if key in dict:
        print(dict[key])
    else:
        p = help[j]
        dict[key] = f(p)
        print(dict.get(key))