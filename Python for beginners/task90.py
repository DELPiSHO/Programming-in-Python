n = int(input())
numbers = []
for i in range(n):
    a = int(input())
    a = list(reversed(sorted(list(str(a)))))
    numbers.append(a)
for i in numbers:
    
