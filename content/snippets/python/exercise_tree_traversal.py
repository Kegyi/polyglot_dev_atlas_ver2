class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

res = []
inorder(root, res)
print(res)
