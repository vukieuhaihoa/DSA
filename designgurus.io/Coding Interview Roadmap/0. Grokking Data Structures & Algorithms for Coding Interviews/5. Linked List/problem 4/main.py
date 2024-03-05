# class DLNode:
#    def __init__(self, val=0):
#        self.val = val
#        self.next = None
#        self.prev = None

class Solution:
    def isPalindrome(self, head):
        # ToDo: Write your code here.
        if not head or not head.next:
            return True
        tail = head
        while tail.next:
            tail = tail.next
        
        while head != tail and head.next != tail.prev:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.prev
        
        return True
