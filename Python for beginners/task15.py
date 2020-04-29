a = int(input())
b = int(input())
c = int(input())

if b <= a:
    if c <= b:
        print("2 <= 1")
        print("3 <= 2")
    else:
        print("2 <= 1")
elif c <= b:
    print("3 <= 2")
else:
    print("all is good")