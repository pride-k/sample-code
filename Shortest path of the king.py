def letter_to_num(a):
    if a == 'a':
        return 1
    elif a == 'b':
        return 2
    elif a == 'c':
        return 3
    elif a == 'd':
        return 4
    elif a == 'e':
        return 5
    elif a == 'f':
        return 6
    elif a == 'g':
        return 7
    elif a == 'h':
        return 8
    else:
        return int(a)       
start_s = input()
end_s = input()
x = []
y = []
z = []
for i in start_s:
    x.append(letter_to_num(i))
for i in end_s:
    y.append(letter_to_num(i))
n = 0
while x != y:
    if x[0] == y[0]:
        if x[1] < y[1]:
            x[1] += 1
            n += 1
            z.append('U')
        elif x[1] > y[1]:
            x[1] -= 1
            n += 1
            z.append('D')
    elif x[0] < y[0]:
        if x[1] == y[1]:
            x[0] += 1
            n += 1
            z.append('R')
        elif x[1] < y[1]:
            x[0] += 1
            x[1] += 1
            n += 1
            z.append('RU')
        elif x[1] > y[1]:
            x[0] += 1
            x[1] -= 1
            n += 1
            z.append('RD')
    elif x[0] > y[0]:
        if x[1] == y[1]:
            x[0] -= 1
            n += 1
            z.append('L')
        elif x[1] < y[1]:
            x[0] -= 1
            x[1] += 1
            n += 1
            z.append('LU')
        elif x[1] > y[1]:
            x[0] -= 1
            x[1] -= 1
            n += 1
            z.append('LD')
print(n)
print(*z,sep="\n")