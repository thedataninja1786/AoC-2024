from collections import defaultdict

with open("data/day5.txt","r") as f:
    data = f.read()

def parse(data):
    rules,updates = [],[]
    for line in data.splitlines():

        if "|" in line:
            x,y = line.split("|")[0],line.split("|")[1]
            rules.append([int(x),int(y)])
        else:
            if line:
                updates.append([int(x) for x in line.split(",")])
    return rules,updates

# <--------------------------  PART 1  --------------------------> 
rules,updates = parse(data)
good = []
for ls in updates:
    f = True
    ls_cp = ls[:]
    while ls:
        x = ls.pop()
        crules = [rule[0] for rule in rules if rule[1] == x]
        if not ls:
            good.append(ls_cp)
            break
        if ls[-1] not in crules:
            f = False
            break
    if f and ls_cp not in good: good.append(ls_cp)

s = 0 
for ls in good:
    s += ls[len(ls)//2]
print(s)



# <--------------------------  PART 2  -------------------------->
rules,updates = parse(data)
not_good = []
for ls in updates:
    if ls not in good:
        not_good.append(ls)

c = defaultdict(list)
for x,y in rules:
    c[y].append(x)

def bfs(num,tmp):
    q = [num]
    visited = set([num])
    path = [num]
    while q:
        n = q.pop(0)
        for x in c[n]:
            if x not in path and x in tmp: 
                path.insert(0,x)
            if x in tmp and x not in visited:
                q.append(x)
                visited.add(x)
    return len(path)-1

s = 0
for ls in not_good:
    tmp = [0 for _ in range(len(ls))]
    for n in ls:
        idx = bfs(n,ls)
        tmp[idx] = n
    s += tmp[len(tmp)//2]
print(s)

