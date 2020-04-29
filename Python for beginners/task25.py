x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x2 == x1+1 and y2 == y1-1) or (x2 == x1+1 and y2 == y1) or (x2 == x1+1 and y2 == y1+1) or (x2 == x1 and y2 == y1-1) or (x2 == x1 and y2 == y1+1) or (x2 == x1-1 and y2 == y1-1) or (x2 == x1-1 and y2 ==y1) or (x2 == x1-1 and y2 == y1+1)) and (1 <= x2 <= 8 or 1 <= y2 <= 8) and (1 <= x1 <= 8 or 1 <= y1 <= 8):
    print("YES")
else:
    print("NO")