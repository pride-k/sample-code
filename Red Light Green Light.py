n,d,t = input().split()
n = int(n)
d = int(d)
t = int(t)
x = input().split()
green = 0
total = 0 
for i in range(n):
    if total + int(x[i]) >= t:
        if i%2 == 0:
            green = green+(t-total)
        break
    total = total + int(x[i])
    if i%2 == 0:
        green += int(x[i])
if green >= d:
    print("YES")    
else:
    print("NO")
    
