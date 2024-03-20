class Node:
    def __init__(self, value: int, next: 'Node' = None) -> None:
        self.value: int = value
        self.next: Node = next
        
class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self) -> None:
        cur = self.head
        while cur:
            print(f"{cur.value}", end=' -> ')
            cur = cur.next
        print('None')
    
    def make_empty(self) -> None:
        self.head = self.tail = None
        self.length = 0
     
    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        if self.head is None: return None
        tail = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next != tail:
                cur = cur.next
            self.tail = cur
            self.tail.next = None
        self.length -= 1
        return tail

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> Node:
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        temp.next = None
        return temp
    
    def get(self, index: int) -> Node:
        if index < 0 or index >= self.length: return None
        cur = self.head
        for _ in range(index): cur = cur.next
        return cur
    
    def set_value(self, index: int, value: int) -> bool:
        if index < 0 or index >= self.length: return None
        cur = self.head
        for _ in range(index): cur = cur.next
        cur.value = value
        return True    
    
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length: return False
        # insert at the beginning of the LL
        if index == 0:
            return self.prepend(value)
        
        # insert at the end of the LL
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        cur = self.get(index - 1)
        new_node.next = cur.next
        cur.next = new_node
        self.length += 1
        return True
        
def main():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.print_list()    

if __name__ == '__main__':
    main()