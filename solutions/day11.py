from functools import lru_cache
from collections import defaultdict, Counter

"""If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone."""


s = "125 17"
s = "64554 35 906 6 6960985 5755 975820 0"

# <----------------------------------------  PART 1  ---------------------------------------->
for _ in range(26):
    ls = s.split(" ")
    ls = [x for x in ls if x]
    ls = [x.strip("0") if len(x) > 1 and x[0] == "0" else x for x in ls]
    tmp = ""
    for x in ls:
        if x == "0":
            tmp += "1"
            tmp += " "
        elif len(x) > 1 and len(x) % 2 == 0:
            idx = len(x)//2
            tmp += x[:idx]
            tmp += " "
            y = x[idx:].lstrip('0')  
            tmp += y if y else "0"   
            tmp += " "
        else:
            tmp += str(int(x.strip()) * 2024)
            tmp += " "
        
    s = tmp
print(len(ls))

# <----------------------------------------  PART 2  ---------------------------------------->
"""
@lru_cache
def compute(T):
    s = "64554 35 906 6 6960985 5755 975820 0"
    for i in range(T):
        ls = s.split(" ")
        ls = [x for x in ls if x]
        ls = [x.strip("0") if len(x) > 1 and x[0] == "0" else x for x in ls]
        print(i,len(ls))
        tmp = ""
        for x in ls:
            if x == "0":
                tmp += "1"
                tmp += " "
            elif len(x) > 1 and len(x) % 2 == 0:
                idx = len(x)//2
                tmp += x[:idx]
                tmp += " "
                y = x[idx:].lstrip('0')  
                tmp += y if y else "0"   
                tmp += " "
            else:
                tmp += str(int(x.strip()) * 2024)
                tmp += " "
            
        s = tmp
    return len(ls)

print(compute(75))
"""
# lru cache is too slow still 

s = "64554 35 906 6 6960985 5755 975820 0"
ls = [x for x in s.split(" ")]
c = Counter(ls)

for i in range(75):
    tmp = Counter()
    for x in c.keys(): 
        k = c[x]
        if x == "0":
            tmp["1"] += k
        elif len(x) > 1 and len(x) % 2 == 0:
            idx = len(x)//2
            y = x[:idx]
            tmp[y] += k
            y = x[idx:].lstrip('0')  
            y = y if y else "0"
            tmp[y] += k   
        else:
            y = str(int(x.strip()) * 2024)
            tmp[y] += k

    c = tmp.copy()
print(sum(c.values()))