print("Hello IIIT Delhi")
print("Hello Delhi")
print("Hello World")

T1 = float(input("Time 1? "))
T2 = float(input("Time 2? "))
if T1 > T2:
    minT = T2
else:
    minT = T1
print(T1, T2, minT)

def MinTime(T1,T2,T3):
    minT =  T1
    if (T2 < minT):
        minT = T2
    if (T3 < minT):
        minT = T3
    return(minT)
T1 = float(input("Time 1: "))
T2 = float(input("Time 2: "))
T3 = float(input("Time 3: "))
minT = MinTime(T1,T2,T3)
print(minT)