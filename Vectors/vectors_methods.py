
def add_vectors(list1, list2):
    if list1 is None or list2 is None: return None
    if len(list1) == len(list2):
        list = []
        for (i,v) in enumerate(list1):
            list.append(v + list2[i])
        return list
    else:
        return None

def scalar_mult(s, v):
    if v is None: return None
    list = []
    for e in v:
        list.append(e * s)
    return list

def dot_product(u, v):
    if u is None or v is None: return None
    if len(u) == len(v):
        product = 0
        for (i,value) in enumerate(u):
            product += value * v[i]
        return product
    else:
        return None
    
def cross_product(u, v):
    if u is None or v is None: return None
    if len(u) == len(v) == 3:
        return [(u[1]*v[2])-(u[2]*v[1]), (u[2]*v[0])-(u[0]*v[2]), (u[0]*v[1])-(u[1]*v[0])]
    else:
        return None

def replace(s, old, new):
        if old == "": return s
        l = list(s)
        for (i,v) in enumerate(l):
            a = l[i:i+len(old)]
            if a == list(old):
                l[i:i+len(old)] = list(new)
        return "".join(l)

def swap(x, y): 
    # print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    # print("after swap statement: x:", x, "y:", y)
    return (x, y)
