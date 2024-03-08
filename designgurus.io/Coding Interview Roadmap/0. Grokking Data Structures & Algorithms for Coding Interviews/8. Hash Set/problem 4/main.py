class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        maxLength = 0
        # ToDo: Write Your Code Here.
        l = 0
        for r in range(len(s)):
            if s[r] in char_set:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength