from collections import defaultdict

data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

data = """Register A: 46187030
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0"""

c = defaultdict(int)

for line in data.split("\n\n")[0].splitlines():
    k = line.split(":")[0][-1]
    v = line.split(":")[1].strip()
    c[k] = int(v)


ls = [x for x in data.split("\n\n")[-1].split(": ")[1]]
ls = [int(x) for x in ls if x != ","]

i = 0 
res = []

d = {4:"A",5:"B",6:"C"}

while i < len(ls):
    print(c)
    
    x,y = ls[i],ls[i+1]
    
    if y > 3:
        y = c[d[y]]

    if x == 0:
        z = c["A"] // (2**y) 
        c["A"] = z
    elif x == 1:
        c["B"] = y ^ c["B"]
    elif x == 2:
        z = y % 8 
        c["B"] = z
    elif x == 3:
        if c["A"] != 0:
            i = y   
            continue
    elif x == 4:
        z= c["B"] ^ c["C"]
        c["B"] = z
    elif x == 5:
        print(y)
        res.append(y%8)
    elif x == 6:
        z = c["A"] // (2**y)
        c["B"] = z
    elif x == 7:
        z = c["A"] // (2**y) 
        c["C"] = z
         
    i += 2

print(res)
print(",".join([str(x) for x in res]))