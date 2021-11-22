import sys
input = sys.stdin.readline

num = int(input())
arr = dict()

for _ in range(num):
    node, left, right = input().split()
    arr[node] = [left,right]

def preorder(root):
    if root != '.':
        print(root,end='')
        preorder(arr[root][0])
        preorder(arr[root][1])

def inorder(root):
    if root != '.':
        inorder(arr[root][0])
        print(root,end='')
        inorder(arr[root][1])

def postorder(root):
    if root != '.':
        postorder(arr[root][0])
        postorder(arr[root][1])
        print(root,end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
