def get_winner(a, b, c, d = 0, e = 0):
    if max(a,b,c,d,e) == a:
        return "Первый"
    elif max(a,b,c,d,e) == b:
        return "Второй"
    elif max(a,b,c,d,e) == c:
        return "Третий"
    elif max(a,b,c,d,e) == d:
        return "Четвертый"
    else:
        return "Пятый"
m = get_winner(int(input()),int(input()),int(input()),int(input()),int(input())).split(',')
print(*m)

