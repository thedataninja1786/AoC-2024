data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

with open("data/day25.txt","r") as f:
    data = f.read()


locks,keys= [],[]
for line in data.split("\n\n"):
    ls = [list(x) for x in line.splitlines()]
    if len(set(ls[0])) == 1 and ls[0][0] == "#":
        locks.append(ls)
    else:
        keys.append(ls)


def find_dims(ls):  
    out = []
    for j in range(len(ls[0])):
        cnt = -1
        for i in range(len(ls)):
            if ls[i][j] == "#":
                cnt += 1
        out.append(cnt)
    return out

keys_dims,lock_dims = [],[]

for ls in keys:
    keys_dims.append(find_dims(ls))
for ls in locks:
    lock_dims.append(find_dims(ls))

def check(ls,ds):
    for i in range(len(ls)):
        if ls[i]+ds[i] >= 6:
            return False
    return True

res = 0
for k in keys_dims:
    for l in lock_dims:
        if check(k,l):
            res += 1 
print(res)

