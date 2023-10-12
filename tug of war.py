n, r = input().split()
n = int(n)
r = int(r)
x = input().split()
x = tuple([int(i) for i in x])
ans = 0
for i in range(n+1):
    for j in range(i):
        y = sum(x[j:i])
        if y%r == 0:
            ans += 1
print(ans)