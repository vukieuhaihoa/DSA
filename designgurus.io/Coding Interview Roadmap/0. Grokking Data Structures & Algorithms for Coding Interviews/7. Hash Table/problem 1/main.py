class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ToDo: Write Your Code Here.
        d = collections.defaultdict(int)
        for ch in s:
            d[ch] += 1
                    
        for i, ch in enumerate(s):
            if d[ch] == 1:
                return i
        return -1