


n = int(input())
arr = list(map(int,input().split()))
tree = [[] for _ in range(n)]

def make(arr,x):
    print(arr,x)
    mid = len(arr)//2
    tree[x].append(arr[mid])
    if len(arr) == 1: return
    make(arr[:mid], x + 1)
    make(arr[mid +1:], x + 1)

make(arr,0)
print(tree)