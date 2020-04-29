n = int(input())
for i in range(1, n):
    if i != 1 and n % i == 0:
        print("Составное")
        break;
else:
    print("Простое")