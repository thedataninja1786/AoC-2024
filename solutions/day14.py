from collections import defaultdict
from math import prod

data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

with open("data/day14.txt","r") as f:
    data = f.read()

def process_data():
    I,J = 0,0
    positions = defaultdict(tuple)
    velocities = defaultdict(tuple)
    for x,line in enumerate(data.splitlines()):
        l = "".join(line.split("p=")[1]).split("v=")[0].strip()
        i,j = l.split(",")
        i = int(i); j = int(j)
        positions[x] = (j,i)
        I = max(I,i)
        J = max(J,j)
        l = "".join(line.split("p=")[1]).split("v=")[1].strip()
        vi,vj = l.split(",")
        vi = int(vi); vj = int(vj)
        velocities[x]=(vj,vi)
        
    grid = [[0 for _ in range(I+1)] for _ in range(J+1)]

    for k,v in positions.items():
        i,j = v
        grid[i][j] += 1
    
    return grid,positions,velocities
# <---------------------------------------------------  PART 1  --------------------------------------------------->
grid,positions,velocities = process_data()
def simulate(grid,N):
    for _ in range(N):
        for k,v in positions.items():
            i,j = v
            grid[i][j] = max(grid[i][j]-1,0)
            vi,vj = velocities[k]
            i = (i + vi) % len(grid)
            j = (j + vj) % len(grid[0])
            grid[i][j] += 1
            positions[k] = (i,j)
    return grid

grid = simulate(grid,100)

r = len(grid) // 2
c = len(grid[0]) // 2

res = []
ls = grid[:r]
# top left
s = 0
for l in ls:
    s += sum(l[:c])
res.append(s)
# top right
s = 0
for l in ls:
    s += sum(l[c+1:])
res.append(s)
# bottom left
s = 0
ls = grid[r+1:]
for l in ls:
    s += sum(l[:c])
res.append(s)
# bottom right
s = 0
for l in ls:
    s += sum(l[c+1:])
res.append(s)
print(prod(res))

# <---------------------------------------------------  PART 2  --------------------------------------------------->
grid,positions,velocities = process_data()
cnt = 0
# unknown shape, write to file and check
for _ in range(100000):
    for k,v in positions.items():
        i,j = v
        grid[i][j] = max(grid[i][j]-1,0)
        vi,vj = velocities[k]
        i = (i + vi) % len(grid)
        j = (j + vj) % len(grid[0])
        grid[i][j] += 1
        positions[k] = (i,j)
    cnt += 1
    
    tmp = ""
    for l in grid:
        l = "".join(["*" if x != 0 else "." for x in l])
        tmp += l + "\n"

    with open("grids.txt","a") as f:
        f.write(str(cnt) + "\n")
        f.write(tmp + "\n")

"""
.*................................................................................*.................*
............................*******************************..........*...............................
............................*.............................*.......................*...........*......
............*...............*.............................*..........................................
............**..............*.............................*.......................*..................
............................*.............................*..........................................
............................*..............*..............*........................*...............*.
............................*.............***.............*..........................................
............................*............*****............*..........................................
.......*....................*...........*******...........*..........................................
............................*..........*********..........*..........................................
..............*.............*............*****............*..........................................
...............*............*...........*******...........*..............*...........................
............................*..........*********..........*.................................*........
............................*.........***********.........*..........................................
......................*.....*........*************........*..........................................
.........................*..*..........*********..........*..........................................
............................*.........***********.........*..........................................
............................*........*************........*..........................................
............................*.......***************.......*..........................................
.........*..................*......*****************......*..........................................
.......*..........*.........*........*************........*.....................................*....
........*...................*.......***************.......*..........................................
............................*......*****************......*...*......................................
...............*............*.....*******************.....*.....................*....................
............*...............*....*********************....*.*........................................
............................*.............***.............*.........................*................
.................*.......*..*.............***.............*.........*................................
............................*.............***.............*..........................................
.....................*......*.............................*..........................................
...................*........*.............................*..........................................
..............*.............*.............................*..........................................
............................*.............................*..........................................
............................*******************************..........................................
"""