from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        # ToDo: Write Your Code Here.
        d = defaultdict(int)
        for n in A:
            d[n] += 1
        for n in A:
            if d[n] == 1 and n > maxUnique:
                maxUnique = n
        return maxUnique