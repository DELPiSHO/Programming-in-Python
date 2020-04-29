words = []

with open('dataset_3363_3.txt') as input:
    for line in input:
        words += line.strip().lower().split()
n = 0
w = []

for word in set(words):
    count = words.count(word)
    if count >= n:
        if count > n:
            w = []
        n = count
        w.append(word)

print(min(w),n)