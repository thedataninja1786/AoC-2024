with open("data/day3.txt","r") as f:
    data = f.read()

#data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def check_valid(s):
    if s[-1] == ")":
        i = 4
        n1,n2 = "",""
        while i < len(s):
            if s[i].isnumeric():
                n1 += s[i]
                i += 1
            else: break
        if s[i] == "," and n1.isnumeric():
            i += 1
        else: return [False,0]
        while i < len(s)-1:
            if s[i].isnumeric():
                n2 += s[i]
                i += 1
            else:
                return [False,0]
        return [True, int(n1) * int(n2)]
    else: return [False,0]

# <---------------------------------  PART 1  --------------------------------->

# sliding window
res = 0
j = 0 
for i in range(1,len(data)+1):
    if data[j:i].endswith(")"):
        for z in range(j,i):
            if data[z] == "(" and z - 3 > 0 and data[z-3:z] == "mul":
                s = data[z-3:i]
                f,num = check_valid(s)
                if f: 
                    res += num
                    j = i-1
print(res)

# <---------------------------------  PART 1  --------------------------------->
res = 0
j = 0 
mode = True
for i in range(1,len(data)+1):
    l = i
    while l > 0:
        if "do()" in data[l:i]:
            mode = True
            break
        if "don't()" in data[l:i]:
            mode = False
            break
        l -= 1

    if data[j:i].endswith(")"):
        for z in range(j,i):
            if data[z] == "(" and z - 3 > 0 and data[z-3:z] == "mul":
                s = data[z-3:i]
                f,num = check_valid(s)
                if f and mode:
                    res += num
                    j = i-1
print(res)

