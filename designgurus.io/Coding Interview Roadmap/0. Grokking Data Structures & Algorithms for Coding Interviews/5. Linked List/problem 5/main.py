class Node:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def swapPairs(self, head: Node) -> Node:
        # TODO: Write your code here
        dummy = Node(next = head)
        prev, cur = dummy, head

        while cur and cur.next:
            next_pair = cur.next.next
            second = cur.next

            # swap step
            prev.next = second
            second.next = cur
            cur.next = next_pair

            prev = cur
            cur = next_pair
        
        return dummy.next
