import ast
from collections import defaultdict

with open("data/day7.txt","r") as f:
    data = f.read()

tmp = []

for line in data.splitlines():
    #print(line.split(":"))
    val = int(line.split(":")[0].strip())
    ls = "".join(line.split(":")[1:])
    ls = [x.strip() for x in ls.split(" ") if x]
    ls = [int(x) for x in ls]
    tmp.append((ls,val))

# <------------------------------------  PART 1  ------------------------------------>
res = set()

def dfs(i,s,ls,t):
    global res 

    if i >= len(ls) and s != t:
        return False
    if i == len(ls) and s == t:
        res.add(t)
        return True
    
    dfs(i+1,s + ls[i],ls,t)
    dfs(i+1,s * ls[i],ls,t)

    return False

for ls,t in tmp:
    dfs(0,0,ls,t)

print(sum(res))

# <------------------------------------  PART 2  ------------------------------------>
res = set()

def dfs(i,s,ls,t):
    global res 
    if "".join([str(x) for x in ls]) == str(t):
        res.add(t)
        return 
    if i >= len(ls) and s != t:
        return 
    if i == len(ls) and s == t:
        res.add(t)
        return
        
    dfs(i+1,s + ls[i],ls,t)
    dfs(i+1,s * ls[i],ls,t)
    dfs(i+1,int(str(s) + str(ls[i])),ls,t)

for ls,t in tmp:
    dfs(0,0,ls,t)

print(sum(res))

