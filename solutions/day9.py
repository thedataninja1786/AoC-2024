with open("data/day9.txt","r") as f:
    data = f.read()
s = data.strip()
#s = "2333133121414131402"

# <----------------------------  PART 1  ---------------------------->
res = []
i = 0
for j, x in enumerate(s):
    x = int(x)
    if j % 2 == 0:
        res.extend([str(i)] * x)
        i += 1
    else: 
        res.extend(["."] * x)

q = res[:]
i = 0 
while i < len(res):
    if res[i] == ".":
        while res[i] == ".":
            res[i] = q.pop()
            res = res[:-1]
    i += 1

t = 0
for i in range(len(res)):
    if res[i].isdigit():
        t += int(res[i]) * i

print(t)


# <----------------------------  PART 2  ---------------------------->
res = []
i = 0
for j, x in enumerate(s):
    x = int(x)
    if j % 2 == 0:
        res.extend([str(i)] * x)
        i += 1
    else: 
        res.extend(["."] * x)


visited = set()
i = len(res)-1
while i >= 0:
    if res[i] == "." or res[i] in visited:
        i -= 1
        continue
    else:
        cnt = 1
        j = i-1
        visited.add(res[i])
        while res[j] == res[i]:
            j -= 1
            cnt += 1
            
        for k in range(j):
            if res[k] == ".":
                ccnt = 1
                z = k
                while z <= j and res[k] == ".":
                    k += 1
                    ccnt += 1
                
                if ccnt > cnt:
                    for a in range(z,z+cnt):
                        res[a] = res[i]
                    for a in range(j+1,i+1):
                        res[a] = "."
                    
                    break

        i -= 1

t = 0
for i in range(len(res)):
    if res[i].isdigit():
        t += int(res[i])*i

print(t)
