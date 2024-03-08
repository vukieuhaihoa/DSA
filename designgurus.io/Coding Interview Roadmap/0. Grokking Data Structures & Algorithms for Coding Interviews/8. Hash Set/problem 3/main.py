from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        # ToDo: Write Your Code Here.
        freq_count = Counter(arr)
        return len(set(arr)) == len(set(freq_count.values()))