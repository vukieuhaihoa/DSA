# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

# Approach 1: This is my solution that I tried to figure out
# Good job Hoa, You are making progress gradually 
# mày đang tiến bộ dần dần rồi đó cu, cố lên nào
# class Solution:     
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         # base case
#         if t1 is None and t2 is None:
#             return t1

#         t1.val += t2.val

#         if t1.left is None: 
#             if t2.left is not None:
#                 t1.left = t2.left
#         else:
#             if t2.left is not None:
#                 self.mergeTrees(t1.left, t2.left)
        
#         if t1.right is None:
#             if t2.right is not None:
#                 t1.right = t2.right
#         else:
#             if t2.right is not None:
#                 self.mergeTrees(t1.right, t2.right)
        
#         return t1


# Approach 2: After viewed solution
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # ToDo: Write Your Code Here.
        if t1 is None:
            return t2

        if t2 is None:
            return t1
        
        new_node = TreeNode(t1.val + t2.val)
        new_node.left = self.mergeTrees(t1.left, t2.left)
        new_node.right = self.mergeTrees(t1.right, t2.right)
        return new_node
