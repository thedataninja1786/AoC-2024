data = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

with open("data/day15.txt","r") as f:
    data = f.read()

grid,dirs = [],[]
tmp = []
for i,line in enumerate(data.splitlines()):
    if line: tmp.append(list(line))
    else:
        grid = tmp[:]
        tmp = []
dirs = tmp[:]
dirs = [x for ls in dirs for x in ls]

# starting position
f = True
for i in range(len(grid)):   
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            grid[i][j] = "."
            f = False
            break
    if not f: break


c = {">":[0,1],"<":[0,-1],"^":[-1,0],"v":[1,0]}

x,y = i,j
for d in dirs:
    dx, dy = x + c[d][0], y + c[d][1]

    if not (0 <= dx < len(grid) and 0 <= dy < len(grid[0])):
        break
    
    if grid[dx][dy] == "#":
        continue
    elif grid[dx][dy] == ".":
        x, y = dx, dy
    else:
        tmpx, tmpy = dx, dy 
        f = True
        # increment till the last box 
        while grid[dx][dy] == "O":
            dx += c[d][0]
            dy += c[d][1]

            # do not update if we hit a wall i.e. no room!
            if grid[dx][dy] == "#":
                f = False
                break
        if f:
            grid[dx][dy] = "O" 
            grid[tmpx][tmpy] = "."
            x,y = tmpx,tmpy

s = 0 
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            s += (100 * i) + j


print(s)
