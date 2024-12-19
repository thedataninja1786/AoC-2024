from functools import lru_cache
data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

with open("data/day19.txt","r") as f:
    data = f.read()  


ls = data.split("\n\n")[0].split(",")
ls = set([x.strip() for x in ls])
data = data.split("\n\n")[1]
designs = []
for line in data.splitlines():
    designs.append(line)


# <---------------------------------  PART 1  --------------------------------->
res= set()

def dfs(i,s):
    global design
    if s in c:
        return c[s]
    
    if s == design:
        res.add(s)
        return True

    for j in range(i,len(design)):
        if design[i:j+1] in ls:
            dfs(j+1,s+design[i:j+1])
            c[s] = True

    c[s] = False
    return False

for design in designs:
    c = {}
    dfs(0,"")
print(len(res))

# <---------------------------------  PART 2  --------------------------------->
# count all possibilities 
c = {}
res = 0
def dfs(i,s):
    global design

    if i in c:
        return c[i]
    if s == design:
        return 1
    
    cnt = 0
    for j in range(i,len(design)):
        if design[i:j+1] in ls:
            cnt += dfs(j+1,s + design[i:j+1])
    
    c[i] = cnt
    return cnt

for design in designs:
    c = {}
    res += dfs(0,"")

print(res)