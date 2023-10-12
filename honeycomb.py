x1, y1 = input().split()
x2, y2 = input().split()
x1  = int(x1)
x2  = int(x2)
y1  = int(y1)
y2  = int(y2)
x = max(abs(x2-x1+1),abs(x2-x1-1))
y = max(abs(y2-y1+1),abs(y2-y1-1))
if x1 == x2:
    print(y*2+4)
elif y1 == y2:
    print(x*2+4)
else:
    print((x+y)*2)