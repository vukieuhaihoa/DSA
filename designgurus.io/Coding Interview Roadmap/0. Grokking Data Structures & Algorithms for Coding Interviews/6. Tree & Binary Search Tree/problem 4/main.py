#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # ToDo: Write Your Code Here.
        if root is None:
            return 0
        range_sum_left = self.rangeSumBST(root.left, L, R)
        range_sum_right = self.rangeSumBST(root.right, L, R)

        if L <= root.val <= R:
            return root.val + range_sum_left + range_sum_right
        return range_sum_left + range_sum_right