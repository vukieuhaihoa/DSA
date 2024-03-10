#class TreeNode:
#    def __init__(self, x):
#        self.val = x          # Value stored in the node.
#        self.left = None      # Reference to the left child.
#        self.right = None     # Reference to the right child.

# Approach 1:
# class Solution:
#     def traversal(self, root, lst):
#         if root is None:
#             return lst
#         self.traversal(root.left, lst)
#         lst.append(root.val)
#         self.traversal(root.right, lst)
#         return lst
#     def closestValue(self, root: TreeNode, target: float) -> int:
#         closest_val = root.val
#         # ToDo: Write Your Code Here.
#         lst = self.traversal(root, [])
#         temp = target - lst[0]        
#         for i in range(1, len(lst)):
#             val = abs(target - lst[i])
#             if val < temp:
#                 closest_val = lst[i]
#                 temp = val
#         return closest_val

# Approach 2: After viewed solution:
#class TreeNode:
#    def __init__(self, x):
#        self.val = x          # Value stored in the node.
#        self.left = None      # Reference to the left child.
#        self.right = None     # Reference to the right child.


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest_val = root.val
        # ToDo: Write Your Code Here.
        cur = root
        while cur:
            if abs(cur.val - target) < abs(closest_val - target):
                closest_val = cur.val
 
            if target > root.val:
                cur = cur.right
            else:
                cur = cur.left
        return closest_val

        """Nếu target > cur.val thì mình tìm về phía bên phải. 
        Tại sao? ví dụ cây hiện tại là 
            Tree: 
                  5
                /    \
                3     8
               / \   / \
              1   4 6   9

            target là 6.4
            bắt đầu tại node 5 vì 6.4 > 5 nên mình phải đi về phía bên phải của cây(do bài này là BST mới có tính chất này nhó) mới tìm đc node có độ chênh lệch thấp hơn do node bên phải có giá trị lớn hơn node hiên tại. Nếu đi về bên trái thì giá trị tuyệt đối của nó(abs(cur.val - target)) càng lớn hơn chứ không thể nào nhỏ hơn được         
        """