import heapq

data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
#6x6

with open("data/day18.txt","r") as f:
    data = f.read()

# 70x70

grid = [["." for _ in range(71)] for _ in range(71)]

coords = []
for l in data.splitlines():
    c,r = l.split(",")
    coords.append((int(r),int(c)))


def djikstra(i,j,R,C):
    visited = set()
    coords = [[1,0],[-1,0],[0,1],[0,-1]]
    q = []

    heapq.heappush(q,(0,i,j))
    while q:
        s,x,y = heapq.heappop(q)
        if x == R and y == C:
            return s
        if (x,y) in visited:
            continue
        visited.add((x,y))

        for c in coords:
            dx = x + c[0]
            dy = y + c[1]

            if 0<=dx<len(grid) and 0<=dy<len(grid[0]) and grid[dx][dy] != "#" and (dx,dy) not in visited:
                heapq.heappush(q,(s+1,dx,dy))
                
    return float("inf")

# <------------------------------------------------  PART 1  ------------------------------------------------>
R,C = len(grid)-1,len(grid[0])-1
for r,c in coords[:1024]:
    grid[r][c] = "#"
print(djikstra(0,0,R,C))

# <------------------------------------------------  PART 2  ------------------------------------------------>
for r,c in coords:
    grid[r][c] = "#"
    s = djikstra(0,0,R,C)  
    if s==float("inf"):
        print(c,r)
        break

