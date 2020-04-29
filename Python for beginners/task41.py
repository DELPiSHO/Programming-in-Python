money = int(input())
koszyk = 0
while koszyk <= money:
    n = int(input())
    if koszyk + n >= money:
        print("Стоп, Джон!")
        print(koszyk)
    else:
        koszyk += n
