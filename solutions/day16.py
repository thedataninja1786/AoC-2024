import heapq
from functools import lru_cache
data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

with open("data/day16.txt","r") as f:
    data = f.read()

grid = [list(x)for x in data.splitlines()]
i,j = 0,0
for i in range(len(grid)):
    f = True
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            x,y = i,j
            f = False
            break
    if not f: break

def bfs(i, j):
    # generate all paths with directions slow
    paths = set()  
    coords = [[1, 0],[-1, 0],[0, 1],[0, -1]]  
    q = [[i,j,1000,[(i, j)],0,None]]  # x, y, score, path, cnt_turns, last_direction

    while q:
        x,y,s,path,cnt,last_dir = q.pop(0)

        if grid[x][y] == "E":
            paths.add((tuple(path), s, cnt))

        for c in coords:
            dx = x + c[0]
            dy = y + c[1]

            if 0 <= dx < len(grid) - 1 and 0 <= dy < len(grid[0]) - 1 and grid[dx][dy] != "#" and (dx, dy) not in set(path):
                new_dir = (dx - x, dy - y) 

                new_s, new_cnt = s + 1, cnt
                if last_dir and last_dir != new_dir:
                    new_s += 1000
                    new_cnt += 1

                q.append([dx, dy, new_s, path + [(dx, dy)], new_cnt, new_dir])

    paths = sorted(paths, key=lambda x: x[1])
    return paths[0][1]
    

def djikstra(i,j):
    coords = [[1, 0],[-1, 0],[0, 1],[0, -1]]  
    visited = set()
    q = []
    heapq.heappush(q,(1000,i,j,[(i,j)],0,None))# score, x, y, path, cnt_turns, last_direction

    while q:
        s,x,y,path,cnt,last_dir = heapq.heappop(q)
        if grid[x][y] == "E":
            return s,path,cnt
    
        visited.add((x,y,last_dir))

        for c in coords:
            dx = x + c[0]
            dy = y + c[1]
            if 0 <= dx < len(grid) - 1 and 0 <= dy < len(grid[0]) - 1 and grid[dx][dy] != "#":
                new_dir = (dx-x,dy-y)
                
                new_s,new_cnt = s+1, cnt
                if last_dir and last_dir != new_dir:
                    new_s += 1000
                    new_cnt += 1
                
                if (dx,dy,new_dir) not in visited:
                    heapq.heappush(q, (new_s,dx, dy, path + [(dx,dy)], new_cnt, new_dir))   
        
    return None,[],-1

print(djikstra(x,y))