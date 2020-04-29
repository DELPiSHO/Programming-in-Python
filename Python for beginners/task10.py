from math import *

a = float(input())
b = float(input())
c = float(input())
p = 1/2 * (a + b + c)
S = sqrt(p * (p - a) * (p - b) * (p - c))
print(S)