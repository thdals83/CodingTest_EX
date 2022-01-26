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
class Codec:
    def serialize(self, root):
        res = ["#"]
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                res.append(str(node.val))
            else:
                res.append("None")

        return ' '.join(res)

    def deserialize(self, data):
        print(data)
        if data == "# None": return None
        nodes = data[1:len(data)].split()

        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        idx = 1

        while queue:
            node = queue.popleft()
            if nodes[idx] != 'None':
                node.left = TreeNode(int(nodes[idx]))
                queue.append(node.left)
            idx += 1

            if nodes[idx] != 'None':
                node.right = TreeNode(int(nodes[idx]))
                queue.append(node.right)
            idx += 1

        return root

if __name__ == "__main__":
    x = Codec()
    root = [1, 2, 3, null, null, 4, 5]
    inputtree1 = make_tree_by(root, 0)

    print(x.serialize(inputtree1))
    x.deserialize(inputtree1)
