import math
a,b = input().split()
a = int(a)
b = int(b)
x = a
while a >= b:
    x = x + math.trunc(a/b)
    a = math.trunc(a/b) + a%b
print(math.trunc(x))
