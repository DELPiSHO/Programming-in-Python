text = ""
helper = []
while True:
    i = input()
    if i == '.':
        break
    else:
        helper.append(i)
n = int(input())
for i in range(0,n):
    m = int(input())
    text += helper[m-1]
print(text)
