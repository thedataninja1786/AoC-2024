with open("data/day2.txt","r") as f:
    data = f.read()

ls = []
for l in data.splitlines():
    ls.append([int(x) for x in l.split(" ")])

# <-------------------------------  PART 1  ------------------------------->
def check_increasing_decreasing(level):
    increasing = True
    for i in range(1,len(level)):
        if level[i] > level[i-1]:
            continue
        else:
            increasing = False
            break 
    decreasing = True
    for i in range(1,len(level)):
        if level[i-1] > level[i]:
            continue
        else:
            decreasing = False
            break
    return decreasing or increasing

def check_adjacent(level):
    f = True
    for i in range(1,len(level)):
        if 0 < abs(level[i-1] - level[i]) < 4:
            continue
        else:
            f = False
            break
    return f


cnt = 0 
for level in ls:
    if check_increasing_decreasing(level) and check_adjacent(level):
        cnt += 1
print(cnt)

# <------------------------------  PART 2  ------------------------------->
res = 0
while ls:
    level = ls.pop(0)
    l = len(level)
    for i in range(l):
        x = level.pop(i)
        if check_increasing_decreasing(level) and check_adjacent(level):
            res += 1
            break
        else:
            level.insert(i,x)
print(res)

