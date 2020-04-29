line = input().lower().split()
dict = {}
for word in line:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
for word,count in dict.items():
    print(word,count)