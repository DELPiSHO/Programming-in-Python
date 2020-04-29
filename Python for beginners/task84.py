x=[int(i) for i in input().split(',')]
print(sum([i for i in range(len(x)) if x[i]==min(x)]))