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
    def mergeTrees(self, root1: [TreeNode], root2: [TreeNode]) -> [TreeNode]:

        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2

if __name__ == "__main__":
    x = Solution()
    root1 = [1,3,2,5,2,None,None,4]
    root2 = [2,1,3,None,4,None,7]
    inputtree1 = make_tree_by(root1, 0)
    inputtree2 = make_tree_by(root2, 0)
    x.mergeTrees(inputtree1,inputtree2)
