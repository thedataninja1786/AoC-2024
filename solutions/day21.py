data = """935A
319A
480A
789A
176A"""

s = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"

data = """029A
980A
179A
456A
379A"""


c = {7:(0,0),8:(0,1),9:(0,2),4:(1,0),5:(1,1),6:(1,2),1:(2,0),2:(2,1),3:(2,3),0:(3,1)}
x,y = 3,2

res = ""


def numeric_to_positional(s):
    x,y = 0,2
    r = ""
    d = {"^":(0,1),"A":(0,2),"<":(1,0),"v":(1,1),">":(1,2)}
    for l in s:
        dx,dy = d[l]
        nx = dx - x 
        ny = dy - y

        if nx == 0 and ny == 0:
            r += "A"
            continue
        
        for _ in range(abs(nx)):
            if nx > 0:
                r += "v"
            else: r += "^"

        for _ in range(abs(ny)):
            if ny > 0:
                r += ">"
            else: r += "<"
       
        if nx != 0 or ny != 0:
            r += "A" 
        
        x,y = dx,dy
    
    #print(r)
    #assert len("v<<A>>^A<A>AvA<^AA>A<vAAA>^A") == r,  f"{len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')} != {len(r)}"
    return r

ls = ""
ds= ""
for s in data.splitlines():
    res = ""
    ls = ""
    ds = ""
    num = int("".join([x for x in s if x.isdigit()]))
    for l in s:
        tmp = ""
        if l == "A":
            dx,dy = 3,2
        else:
            dx,dy = c[int(l)]
        nx = dx - x
        ny = dy - y 
        
        moved_y = False
        moved_x = False
        for _ in range(abs(ny)):
            if ny > 0:
                tmp += ">"
            else:
                tmp += "<"
            moved_y = True
        if moved_y: tmp += "A"
        for _ in range(abs(nx)):
            if nx > 0:
                tmp += "v"
            else: tmp += "^"
            moved_x = True
        if moved_x: tmp += "A"

        res += tmp
        x,y = dx,dy

    ls += numeric_to_positional(res)
    ds += numeric_to_positional(ls)

    print((len(ds))*num)
    print(res)
    break
print(len(ls))
print(len(ds))
