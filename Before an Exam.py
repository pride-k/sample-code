n1,n2 = input().split()
n1 = int(n1)
n2 = int(n2)
min_time = 0
max_time = 0
x = []
y = []
for _ in range(n1):
    a,b = input().split()
    a = int(a)
    b = int(b)
    x.append(a)
    y.append(b)
    min_time += a
    max_time += b
if n2 > max_time or n2 < min_time:
    print("NO")
else:
    print("YES")
    for i in range(n1):
        print(min(y[i],(x[i]+n2-min_time)),end=" ")
        n2 -= min(y[i],(x[i]+n2-min_time))
        min_time -= x[i]