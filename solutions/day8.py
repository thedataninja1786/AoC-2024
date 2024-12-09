from collections  import defaultdict 

with open("data/day8.txt","r") as f:
    data = f.read()

# <--------------------------------  PART 1  -------------------------------->
grid = [list(x) for x in data.splitlines()]

c = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            c[grid[i][j]].append((i,j))
        

for k in c.keys():
    for i,(x1,y1) in enumerate(c[k]):
        for j in range(len(c[k])):
            x2,y2 = c[k][j]
            if x1 != x2 and y1 != y2:
                dx,dy = x1-x2, y1-y2
                if 0<= x1 + dx < len(grid) and 0<= y1 + dy < len(grid[0]):
                    grid[x1+dx][y1+dy] = "#"               

def count(grid):                
    cnt = 0 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                cnt += 1
    return cnt

print(count(grid))
# <--------------------------------  PART 2  -------------------------------->
grid = [list(x) for x in data.splitlines()]

c = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            c[grid[i][j]].append((i,j))

for k in c.keys():
    for i,(x1,y1) in enumerate(c[k]):
        for j in range(len(c[k])):
            x2,y2 = c[k][j]
            if x1 != x2 and y1 != y2:
                dx,dy = x1-x2, y1-y2
    
                xx1,yy1 = x1 + dx, y1 + dy
                while 0<= xx1 < len(grid) and 0<= yy1 < len(grid[0]):
                    grid[xx1][yy1] = "#"
                    xx1 += dx
                    yy1 += dy
                
                xx1,yy1 = x1 - dx, y1 - dy
                while 0<= xx1 < len(grid) and 0<= yy1 < len(grid[0]):
                    grid[xx1][yy1] = "#"
                    xx1 -= dx
                    yy1 -= dy

print(count(grid))