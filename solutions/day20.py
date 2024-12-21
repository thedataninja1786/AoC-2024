import heapq
from collections import defaultdict
from copy import deepcopy


data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

with open("data/day20.txt","r") as f:
    data = f.read()

grid = [list(x) for x in data.splitlines()]

x,y = 0,0
for i in range(len(grid)):
    f = True
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            x,y = i,j
            f = False
            break
    if not f: break


def djikstra(origin:tuple,grid):
    visited = set()
    coords = [[1,0],[-1,0],[0,1],[0,-1]]
    i,j = origin
    q = [] 
    heapq.heappush(q,(0,i,j))
    while q:
        s,x,y = heapq.heappop(q)
        #if s > res: return -1
        if grid[x][y] == "E":
            return s
        if (x,y) in visited: 
            continue
        visited.add((x,y))

        for c in coords:
            dx,dy = x+c[0],y+c[1]
            if 0< dx<len(grid)-1 and 0 < dy<len(grid[0])-1 and grid[dx][dy] != "#" and (dx,dy) not in visited:
                heapq.heappush(q,(s+1,dx,dy))
    
    return -1


longest = djikstra((x,y),grid)
"""
# part 1
ls = []
cnt  = 0
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        if grid[i][j] == "#":
            grid[i][j] = "."
            z = djikstra((x,y),grid)
            if longest - z > 0:
                ls.append(longest-z)
            
            grid[i][j] = "#"

print(len([x for x in ls if x > 99]))
"""
# part 2
ls = []

def dfs(i,j,cnt):
    global grid_cp
    global visited
    
    if grid_cp[i][j] != "#" or cnt == 20:
        return 
    
    visited.add((i,j))

    coords = [[1,0],[-1,0],[0,1],[0,-1]]
    for c in coords:
        x,y = i + c[0],j+c[1]
        if 0 < x < len(grid)-1 and 0 < y < len(grid[0])-1 and grid_cp[x][y] == "#" and (x,y) not in visited:
            dfs(x,y,cnt+1)


for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        if grid[i][j] == "#":
            grid_cp = deepcopy(grid)
            visited = set()
            dfs(i,j,0)
            for dx,dy in visited:
                grid_cp[dx][dy] = "."
                z = djikstra((x,y),grid_cp)

                if longest - z > 0:
                    ls.append(longest-z)
            
print(len([x for x in ls if x > 99]))

