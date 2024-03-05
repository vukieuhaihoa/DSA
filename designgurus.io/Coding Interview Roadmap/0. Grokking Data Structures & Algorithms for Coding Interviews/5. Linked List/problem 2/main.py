# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # TODO: Write your code here
        curr = head
        while curr:
            if curr.next and (curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
