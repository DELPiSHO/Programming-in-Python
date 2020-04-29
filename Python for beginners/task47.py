n = int(input())
a = int(input())
b = int(input())
k = 0
while b != 0:
    a, b = b, a % b
for i in range (2, n):
    k = int(input())
    while a != k:
        if a > k:
            a //= k
        else:
            k += a
print(k)
