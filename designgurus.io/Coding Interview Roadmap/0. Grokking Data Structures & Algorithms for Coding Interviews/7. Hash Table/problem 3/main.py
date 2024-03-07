from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # ToDo: Write Your Code Here.
        d = defaultdict(int)
        for c in text:
            d[c] += 1
        
        for c in 'balon':
            if d[c] == 0:
                return 0
        
        return d['l'] // 2 if d['l'] < d['o'] else d['o'] // 2
