with open("data/day4.txt","r") as f:
    data = f.read()



word = "XMAS"

grid = []
res = 0 
for line in data.splitlines():
    grid.append(list(line))

# <----------------------------------  PART 1  ----------------------------------->
for i in range(len(grid)):
    for j in range(len(grid[0])):
        
        for x in range(-1,2):
            for y in range(-1,2):
                cnt = 0

                for l in range(len(word)):
                    dx = i + (x * l)
                    dy = j + (y * l)

                    if (0<=dx<len(grid)) and (0<=dy<len(grid[0])) and word[l] == grid[dx][dy]:
                        cnt += 1

                if cnt == len(word):
                    res += 1    
print(res)

# <----------------------------------  PART 2  ----------------------------------->

def check_xmas(i,j):
    if i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(grid) and j + 1 < len(grid[0]):
        s1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
        s2 = grid[i+1][j-1] + grid[i][j] + grid[i-1][j+1]
        if s1 in {"SAM","MAS"} and s2 in {"MAS","SAM"}:
            return True
    return False

res = 0 
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "A" and check_xmas(i,j):
            res += 1
print(res)


