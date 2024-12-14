from collections import defaultdict
from functools import lru_cache
data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

"""
with open("data/day13.txt","r") as f:
    data = f.read()
"""
c = defaultdict(list)
tmp = []
for i,line in enumerate(data.splitlines()):
    if not line:
        c[tmp[-1]].append(tmp[1])
        c[tmp[-1]].append(tmp[0])
        tmp = []
        continue
    
    line = line.split(",")
    line = [x.strip() for x in line]
    y = line[-1]
    x = line[0].split(":")[1].strip()
    
    tmp.append((x,y))
if tmp:
        c[tmp[-1]].append(tmp[1])
        c[tmp[-1]].append(tmp[0])


# part 1
res = 0
for k,v in c.items():
    v = [list(x) for x in v]
    
    x_a = int(v[1][0][1:])
    y_a = int(v[1][1][1:])
    x_b = int(v[0][0][1:])
    y_b = int(v[0][1][1:])
    
    X = int(k[0][2:])
    Y = int(k[1][2:])
    loc = (X,Y)
    
    
    costs = []
    for i in range(1,100):
        for j in range(1,100):
            xt = (x_a*i)+(x_b*j)
            yt = (y_a*i)+(y_b*j)
            if xt == X and yt == Y:
                print(i,j)
                costs.append((i*3+j*1))
            if xt > X or yt > Y:
                break
    res += min(costs) if costs else 0

print(res) 

