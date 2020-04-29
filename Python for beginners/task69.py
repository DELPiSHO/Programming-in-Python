c = '3'
while c != 'Я запомнил':
    c = input()
    if c == 'Линейная':
        print("O(n)")
    elif c == 'Кубическая':
        print("O(n^3)")
    elif c == 'Логарифмическая':
        print("O(log n)")
    elif c == 'Константная':
        print("O(1)")
    elif c == 'Квадратичная':
        print("O(n^2)")
    elif c == 'Я запомнил':
        print("Молодец, Вася!")
        break
