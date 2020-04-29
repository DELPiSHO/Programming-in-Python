import re

def zad3(start, stop, step):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])

print(zad3(2,5.5,0.5))

def zad2(list,n):
    first = []
    nonExist = []
    for i in range(1,n+1):
        first.append(i)
    nonExist.append(set(first) - set(list))
    return nonExist

print(zad2([2,3,7,4,9],10))

def zad1(kod1,kod2):
    parse = lambda i: int(i.replace('-', ''))
    kod1, kod2 = parse(kod1), parse(kod2)
    result = ["%02d-%03d" % divmod(x,1000) for x in range(kod1+1,kod2)]
    return result

print(zad1('79-900','80-155'))