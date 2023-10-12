import math
a,b = input().split()
a = int(a)
b = int(b)
x = a
d = 0
while a >= b:
    if a/b == math.trunc(a/b):
        a = a/b
        x = x + a
    else:
        d = d + (a/b - math.trunc(a/b))*b
        if d >= b:
            d = d - b
            a = math.trunc(a/b) + 1
        else:
            a = math.trunc(a/b)
        x = x + a
        
print(math.trunc(x))
