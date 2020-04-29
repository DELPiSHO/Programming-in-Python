def func(x):
    if x <= -2:
        sum = 1 - (x + 2) ** 2
    elif ((x > -2) and (x <= 2)):
        sum = -(x/2)
    else:
        sum = ((x - 2) ** 2) + 1
    print(sum)

func(4.5)
func(-4.5)
func(1)