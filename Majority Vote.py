n = int(input())
score = {"X":0,"O":0}
x = []
for i in range(n):
    temp = input().split()
    if temp[1] == 'X':
        score['X'] += int(temp[0])
        x.append(int(temp[0]))
    else:
        score['O'] += int(temp[0])
x.sort()
x.reverse()
i = 0
while score['O'] <= score['X']:
    score['O'] += x[i]
    score['X'] -= x[i]
    i += 1 
print(i)
