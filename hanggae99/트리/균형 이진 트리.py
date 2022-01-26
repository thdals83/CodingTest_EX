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
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)
    return parent

# DFS 스택 사용
class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        def check(node):
            if not node: return 0

            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        if check(root) == -1:
            return False
        else:
            return True

if __name__ == "__main__":
    x = Solution()
    root = [3, 9, 20, null, null, 15, 7]
    inputtree1 = make_tree_by(root, 0)
    print(x.isBalanced(inputtree1))
