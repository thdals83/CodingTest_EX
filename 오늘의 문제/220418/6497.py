import sys
# input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0: break

        parents = [i for i in range(m)]
        edges = []
        for _ in range(n):
            x,y,z = map(int,input().split())
            edges.append((z,x,y))

        edges.sort()
        total = 0

        for i in range(len(edges)):
            z, x, y = edges[i]
            if find_parent(x,parents) != find_parent(y,parents):
                union_parent(x,y,parents)
            else:
                total += z
        print(total)
