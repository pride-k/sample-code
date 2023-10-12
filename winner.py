n = int(input())
name1 = []
score1 = []
dict1 = {}
for i in range(n):
    name, score = input().split()
    score = int(score)
    name1.append(name)
    score1.append(score)
    if name not in dict1:
        dict1[name] = score
    else:
        dict1[name] = dict1[name] + score
max_score = max(dict1.values())
potential = []
for (name2,score2) in dict1.items():
    if score2 == max_score:
        potential.append(name2)
new = {}
for i in range(n):
    if name1[i] in potential:
        if name1[i] in new:
            new[name1[i]] += score1[i]
        else:
            new[name1[i]] =  score1[i]
        if new[name1[i]] >= max_score:
            print(name1[i])
            break

    
        
'''
dict2 = sorted(dict1.items(), key=lambda x:x[1])
if dict2[-1][1] == dict2[-2][1]:
    m = dict2[-1][1]
    for i in range(2,len(name1)):
        if m == dict2[-i]:
            n = i
        else:
            break
    for i in dict1.keys[-1:-n]:
        
    for i in name1[-1:-n]:
        
        continue
    
else:
    print(dict2[-1][0])
'''
