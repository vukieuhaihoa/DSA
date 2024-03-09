#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def traversal(self, root, lst):
        if root is None:
            return lst
        self.traversal(root.left, lst)        
        lst.append(root.val)
        self.traversal(root.right, lst)
        return lst
    def minDiffInBST(self, root):
        min_diff = float('inf')
        #ToDo: Write Your Code Here.
        lst = self.traversal(root, [])
        n = len(lst)
        for i in range(1, n):
            min_diff = min(min_diff, abs(lst[i] - lst[i - 1]))
        return min_diff
