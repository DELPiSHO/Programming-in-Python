n = int(input())
places = []
iter = 1
digits = []
for i in range(n):
    a = input().replace(',','').split(' ')
    places.append(a)
for i in places:
    for y in i:
        if iter == 3:
            iter = 0
        if y.isdigit():
            digits.append(y)
        iter += 1
print(digits)
print(places[:2])