n = int(input())-2
k = 2
m = 0
while n>0:
    if n-k>=k+k:
        k += k
        n -= k
        m += 1
    elif n>=k:
        for i in range(2,k+1):
            if k%i == 0:
                n -= i
                k += k
                m += 1
    else:
        for i in range(k,1,-1):
            if k%i == 0:
                n -= i
                k += k
                m += 1
            break
if m%2 != 0:
    print("ALICE")
else:
    print("BOB")