listing = [int(f) for f in input().split()]
for f in range(len(listing) - 1):
    some = 0
    for g in range(f + 1, len(listing)):
        if listing[f] > listing[g]:
            some = listing[f]
            listing[f] = listing[g]
            listing[g] = some
print(*listing)