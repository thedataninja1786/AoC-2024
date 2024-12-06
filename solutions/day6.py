from collections import defaultdict
from copy import deepcopy

with open("data/day6.txt","r") as f:
    data = f.read()

grid = [list(x) for x in data.splitlines()]
f = 0
coords = []

# <---------------------------------------------  PART 1  --------------------------------------------->
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            sp = (i,j)
            break

coords.append(sp)
i,j = sp
while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
    if grid[i][j] == "#":
        if f == 0:
            i += 1 
        elif f == 90:
            j -= 1 
        elif f == 270:
            j += 1 
        elif f == 180:
            i -= 1
        f = (f+90) % 360
       
    else:
        if f == 0:
            i -= 1
        elif f == 90:
            j += 1
        elif f == 180:
            i += 1
        elif f == 270:
            j -= 1
    
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) not in coords and grid[i][j] != "#":
        coords.append((i,j))

print(len(coords))

# <---------------------------------------------  PART 2  ---------------------------------------------> 
def walk(x,y,grid):
    i,j = x,y
    f = 0
    visited = set([x,y,f])
    
    while 0 <= i < len(grid) and 0 <= j < len(grid[0]):

        if grid[i][j] == "#":
            if f == 0:
                i += 1 
            elif f == 90:
                j -= 1 
            elif f == 270:
                j += 1
            elif f == 180:
                i -= 1    
            f = (f + 90) % 360
        
        else:
            if f == 0:
                i -= 1
            elif f == 90:
                j += 1
            elif f == 180:
                i += 1
            elif f == 270:
                j -= 1

        if (i,j,f) in visited:
                return True
        visited.add((i,j,f))
    return False

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            sp = (i,j)
            break

cnt = 0 
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            grid_cp = deepcopy(grid)
            grid_cp[i][j] = "#"
            if walk(sp[0],sp[1],grid_cp):
                cnt += 1
print(cnt)
