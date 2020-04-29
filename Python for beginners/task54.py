a = input()
spis = []
sum = 0
new = a.replace('.',' ')
print(new)
new = new.split()
for i in new:
    sum += int(i)
print(sum)