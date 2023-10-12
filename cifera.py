k = int(input())
l = int(input())
x = 0
for i in range(31):
    if k**i == l:
        x = 1
        break
if x == 1:
    print("YES")
    print(i-1)
else:
    print("NO")
