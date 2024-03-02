import json
from collections import deque

class Solution:
    def __init__(self, v1, v2):
        # ToDo: Write Your Code Here.
        self.dq = deque()
        while v1 and v2:
            self.dq.append(v1.pop(0))
            self.dq.append(v2.pop(0))
        
        while v1:
            self.dq.append(v1.pop(0))
        
        while v2:
            self.dq.append(v2.pop(0))        
        
    def next(self):
        # ToDo: Write Your Code Here.
        if self.hasNext():
            return self.dq.popleft() 
        return -1
    
    def hasNext(self):
        # ToDo: Write Your Code Here.
        return not (len(self.dq) == 0) 


def main():
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    for i in (v1, v2):
        print(i)
    res = [(len(v), iter(v)) for v in (v1, v2) if v]
    # print(res)

if __name__ == '__main__':
    main()