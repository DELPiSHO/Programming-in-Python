def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
fibb = fib(n-1)
fact = factorial(n)
suma = 0
suma = fibb + fact
print(suma)