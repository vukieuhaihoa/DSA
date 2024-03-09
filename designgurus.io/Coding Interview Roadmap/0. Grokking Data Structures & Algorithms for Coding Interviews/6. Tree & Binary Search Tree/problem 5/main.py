#class TreeNode:
#    def __init__(self, x):
#        self.val = x       # Value of the node.
#        self.left = None   # Reference to the left child.
#        self.right = None  # Reference to the right child.


class Solution:
    def __init__(self):
        # `count` keeps track of the number of nodes we've traversed in-order.
        self.count = 0
        
        # `result` will hold our final answer.
        self.result = 0

    def traversal(self, root, lst):
        if root is None:
            return lst
        self.traversal(root.left, lst)
        
        lst.append(root.val)
        self.count += 1

        self.traversal(root.right, lst)
        return lst
    # This method is the public API that finds the kth smallest element in a BST.
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # ToDo: Write Your Code Here.
        lst = self.traversal(root, [])
        return lst[k - 1]

