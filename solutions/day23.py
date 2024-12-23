from collections import defaultdict

with open("data/day23.txt","r") as f:
    data = f.read()

c = defaultdict(set)

for line in data.split():
    a,b = line.split("-")
    c[a].add(b)
    c[b].add(a)

# <---------------------------------  PART 1  --------------------------------->
pairs = set()
for k,v in c.items():
    for x in v:
        for k1,v1 in c.items():
            if k in v1 and x in v1:
                ls = sorted([k,x,k1])
                pairs.add((tuple(ls)))

cnt = 0 
for pair in pairs:
    p = list(pair)
    if [x for x in p if x[0] == "t"]:
        cnt += 1
        
print(cnt)
    
# <---------------------------------  PART 2  --------------------------------->
def bfs(k):
    q = [k]

    path = [k]
    while q:
        x = q.pop(0)
        for n in c[x]:
            f = True
            for p in path:
                if p not in c[n]:
                    f = False
                    continue
            
            if n not in path and f:
                path.append(n)
                q.append(n)
    
    #print(path)
    return path,len(path)

res = []
for k,v in c.items():
    res.append(bfs(k))

path = sorted(res,key=lambda x:x[1],reverse=True)[0][0]
print(path)
print(",".join(sorted(path)))

# Second solution because I forgot to join with ","
for line in data.split():
    a,b = line.split("-")
    c[a].add(b)
    c[b].add(a)


res = []
for k,v in c.items():
    for i in range(len(v)):
        tmp = list(v)
        ls = [k]
        
        a = tmp.pop(i)
        ls.append(a)
    
        for y in tmp:
            f = True
            for x in ls:
                if x not in c[y]:
                    f = False
                    break
            if f:
                ls.append(y)

        res.append(ls)

        tmp.insert(i,a)

res = sorted(res,key=lambda x:len(x),reverse=True)[0]
res = ",".join(sorted(res))
print(res)

