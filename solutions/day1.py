from collections import defaultdict

with open("data/question1.txt","r") as f:
    data = f.read().splitlines()


left,right = [],[]
for line in data:
    l,r = line.split(" ")[0],line.split(" ")[-1]
    left.append(int(l))
    right.append(int(r))

# <-------------------------  PART 1  ------------------------->

left.sort()
right.sort()

distance = 0
for l,r in zip(left,right):
    distance += abs(l-r)
print(distance)

# <-------------------------  PART 2  ------------------------->
c = defaultdict(int)

for r in right:
    c[r] += 1

similarity_score = 0
for l in left:
    similarity_score += l * c[l]
print(similarity_score)
