with open("data/day10.txt","r") as f:
    data = f.read()

grid = [list(map(int,list(x))) for x in data.splitlines()]

starts = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            starts.append((i,j))
    
# <-------------------------------------------------------  PART 1  -------------------------------------------------------> 
def dfs(i,j,tmp,paths):
    if tmp and tmp[-1] == 9 and (i,j) not in global_visited:
        global_visited.add((i,j))
        res.add(tuple(paths))
        return

    if (i,j) in visited:
        return 
    visited.add((i,j))

    coords = [[1,0], [-1,0], [0,1], [0,-1]]
    for c in coords:
        x = i + c[0]
        y = j + c[1]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x,y) not in visited and tmp and grid[x][y] - 1 == tmp[-1]:
            dfs(x,y,tmp + [grid[x][y]],paths + [(x,y)])

global_visited = set()
s = 0 
for i,j in starts:
    global_visited = set()
    visited = set() 
    res = set()
    dfs(i,j,[grid[i][j]],[(i,j)])
    s += len(res)
print(s)

# <-------------------------------------------------------  PART 2  -------------------------------------------------------> 
def dfs(i,j,tmp,paths):
    if tmp and tmp[-1] == 9:
        res.add(tuple(paths))
        return

    coords = [[1,0], [-1,0], [0,1], [0,-1]]
    for c in coords:
        x = i + c[0]
        y = j + c[1]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and tmp and grid[x][y] - 1 == tmp[-1]:
            dfs(x,y,tmp + [grid[x][y]],paths + [(x,y)])

s = 0 
for i,j in starts:
    visited = set() 
    res = set()
    dfs(i,j,[grid[i][j]],[(i,j)])
    s += len(res)

print(s)