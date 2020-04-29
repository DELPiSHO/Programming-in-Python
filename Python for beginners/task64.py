stroka = input().lower().replace(" ","")
naodw = stroka[::-1]
if stroka == naodw:
    print("YES")
else:
    print("NO")

