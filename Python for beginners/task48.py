n = int(input())
lst = []
for i in range(n):
    if n < 30000:
        num = input()
        if num[-1] == "4":
            lst.append(int(num))
        else:
            continue
    else:
        break
print(min(lst))
