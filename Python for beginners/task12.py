rub = int(input())
kop = int(input())
ilosc = int(input())

new_kop = rub * 100 + kop
sum = new_kop * ilosc
new_rub = sum // 100
new_kopp = sum % 100
print(new_rub, new_kopp)