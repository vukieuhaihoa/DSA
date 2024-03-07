from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ToDo: Write Your Code Here.
        d = defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if d[c] <= 0:
                return False
            d[c] -= 1
        return True 