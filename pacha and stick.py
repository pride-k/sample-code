import math
n = int(input())
if n % 4 == 0:
    print(int(n/4-1))
elif n % 2 == 0:
    print(math.trunc(n/4))
else:
    print(0)
