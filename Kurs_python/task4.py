line = input()
c = line.lower().count('c')
g = line.lower().count('g')

gc = c + g
length = len(line)
gcTeam = float((gc / length) * 100)
print(gcTeam)
