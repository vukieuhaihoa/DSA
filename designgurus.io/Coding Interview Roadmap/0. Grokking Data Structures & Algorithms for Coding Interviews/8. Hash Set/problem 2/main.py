class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        # ToDo: Write Your Code Here.
        s = set(jewels)
        for c in stones:
            if c in s:
                count += 1
        return count