x = int(input())
y = int(input())
list1 = []
for x1,y1 in [(1,1),(1,0),(1,-1),(0,1),(1,0),(-1,1),(-1,0),(-1,-1)]:
    for i in range(1,8):
        if x + i*x1 <=8 and x + i*x1 >=1 and y + i*y1 <=8 and y +i*y1 >=1:
            list1.append((x + i*x1,y +i*y1))
print(list1)