import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

preorder = []
while True:
    node = input().strip()
    if not node: break
    preorder.append(int(node))


def post(start, end):
    if start > end: return

    root = preorder[start]
    idx = start + 1

    while idx <= end:
        if preorder[idx] > root: break
        idx += 1

    post(start + 1, idx - 1)
    post(idx, end)
    print(root)


post(0, len(preorder) - 1)






'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
preorder = []
while True:
    node = input().strip()
    if not node: break
    preorder.append(int(node))

postorder = []
def post(preorder, left,right):
    if left > right: return

    root = preorder[left]
    ls = left + 1
    re = right
    rs = right + 1
    for i in range(right - left + 1):
        if i == 0: continue
        if preorder[left + i] > root:
            rs = i +left
            break
    le = rs - 1
    post(preorder,ls,le)
    post(preorder,rs,re)
    postorder.append(root)


post(preorder, 0, len(preorder) - 1)
for i in postorder:
    print(i)
'''