from collections import defaultdict

with open("data/day22.txt","r") as f:
    data = f.read()
    
ls = [int(x) for x in data.splitlines()]

#ls = [1,2,3,2024]
res = []
M = 16777216
sequences = []

for i in range(len(ls)):
    z = int(str(ls[i])[-1])
    sequence = [(0,z)] # diff,banana
    N = 2000
    s = ls[i]
    while N:
        s = s ^ (s*64)
        s %= M
        tmps = s
        tmps /= 32
        tmps = int(tmps)
        s = tmps ^ s
        s %= M
        s = (s * 2048) ^ s
        s %= M

        # last digit is the bananas
        b = int(str(s)[-1])
        sequence.append([b-sequence[-1][1],b])

        N -= 1

    sequences.append(sequence)
    
    res.append(s)
print(sum(res))

# <----------------------------  PART 2  ----------------------------> 
c = defaultdict(int)
visited = {}

for sequence in sequences:
    for i in range(4,len(sequence)): 
        tmp = sequence[i-4:i]
        z = ",".join([str(x[0]) for x in tmp])
        
        if z not in c or i - visited[z] > 3:
            c[z] += max([x[1] for x in tmp])
            visited[z] = i  

print(max(c.values()))

