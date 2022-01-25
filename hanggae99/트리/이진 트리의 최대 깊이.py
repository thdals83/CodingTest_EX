from collections import deque

# Definition for a binary tree node.
from pyasn1.compat.octets import null

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent


'''
#BFS 큐 사용
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:

        if not root: return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return depth
'''


# DFS 스택 사용
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:

        if not root: return 0
        depth = 0

        stack = [root]
        check  = []
        while stack:
            cur = stack.pop()
            check.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        print(check)
        return depth


if __name__ == "__main__":
    x = Solution()
    root = [3,9,20,null,null,15,7]
    inputtree = make_tree_by(root, 0)
    print(x.maxDepth(inputtree))
