from collections import defaultdict

with open("data/day12.txt","r") as f:
    data = f.read()



grid = [list(x) for x in data.splitlines()]

# Plants of the same type can appear in multiple separate regions, and regions can even appear within other regions.

# find unique regions 
def bfs(i,j,n):
    global t 
    t = grid[i][j]
    grid[i][j] = str(n)
    q = [(i,j)]
    coords = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        x,y = q.pop(0)
        for c in coords:
            dx = x + c[0]
            dy = y + c[1]
            if (dx,dy) not in visited and 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == t:
                q.append((dx,dy))
                visited.add((dx,dy))
                grid[dx][dy] = str(n)

n = 0
t = grid[0][0]
visited = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) in visited: 
            continue
        if grid[i][j] != t:
            n += 1
        
        bfs(i,j,n)
        t = str(n)
        visited.add((i,j))


# part 1
# map regions 
point_loc = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        point_loc[grid[i][j]].append((i,j))


# find the points where the region starts and ends
coords = defaultdict(list)
for k,v in point_loc.items():
    mn = min([x[0] for x in v])
    mx = max([x[0] for x in v])
    tmp = [x for x in v if x[0] == mn]
    top_left = sorted(tmp,key = lambda x: x[1])[0]
    top_right = sorted(tmp,key = lambda x: x[1],reverse=True)[0]

    tmp = [x for x in v if x[0] == mx]
    bottom_left = sorted(tmp,key = lambda x:x[1])[0]
    bottom_right = sorted(tmp,key=lambda x:x[1],reverse=True)[0]

    coords[k] = [[top_left,bottom_left,top_right,bottom_right]]

def find_area_perim(k):
    a = len(point_loc[k])
    
    # use point_locations for each region
    p = 0
    for i,j in point_loc[k]:
        cnt = 4
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for d in dirs:
            x = i + d[0]
            y = j + d[1]

            if (0 <= x < len(grid) and 0 <= y < len(grid[0])) and (x,y) in point_loc[k]:
                cnt -= 1
        p += cnt 
    
    return max(a,1),p

s = 0
for k,_ in point_loc.items():
    
    a,p =find_area_perim(k)
    #print(a,p)
    s += (a*p)
print(s)

# part 2
data = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

grid = [list(x) for x in data.splitlines()]

def bfs(i,j,n):
    global t 
    t = grid[i][j]
    grid[i][j] = str(n)
    q = [(i,j)]
    coords = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        x,y = q.pop(0)
        for c in coords:
            dx = x + c[0]
            dy = y + c[1]
            if (dx,dy) not in visited and 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == t:
                q.append((dx,dy))
                visited.add((dx,dy))
                grid[dx][dy] = str(n)

n = 0
t = grid[0][0]
visited = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) in visited: 
            continue
        if grid[i][j] != t:
            n += 1
        
        bfs(i,j,n)
        t = str(n)
        visited.add((i,j))


for l in grid:
    print(l)

c = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        c[grid[i][j]].append((i,j))

def estimate(k):
    cnt = 0 
    ls = c[k]
    print(ls)
    a = max(1,len(ls))
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    for i,j in ls:
        s = 4
        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if (0 <= x < len(grid) and 0 <= y < len(grid[0])) and (x,y) in ls:
                s -= 1
        cnt += s
    return a,cnt

s = 0
for k in c.keys():
    a,p = estimate(k)
    print(a,p)
    s += (a*p)

print(s)