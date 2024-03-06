from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        # ToDo: Write Your Code Here.
        d = defaultdict(int)
        for num in A:
            d[num] += 1
        
        for k, v in d.items():
            if v == 1 and k > maxUnique:
                maxUnique = k
        return maxUnique