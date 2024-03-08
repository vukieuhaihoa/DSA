
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        # Write Your Code Here.
        s = set(arr)
        for num in arr:
            if num + 1 in s:
                count += 1
        return count