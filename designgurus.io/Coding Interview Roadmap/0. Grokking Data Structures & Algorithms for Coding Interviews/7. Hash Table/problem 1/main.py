from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ToDo: Write Your Code Here.
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        
        for i, c in enumerate(s):
            if d[c] == 1:
                return i            
        return -1