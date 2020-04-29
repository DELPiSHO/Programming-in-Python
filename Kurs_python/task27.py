n = int(input())
teams = []
scorebord = []
points = []
for i in range(n):
    i = input().split(';')
    teams.append(i)

print(teams[1:])
#print(teams.__getitem__(1))