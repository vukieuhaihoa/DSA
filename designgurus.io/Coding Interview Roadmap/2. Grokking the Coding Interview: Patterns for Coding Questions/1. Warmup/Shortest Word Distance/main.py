class Solution:
  def shortestDistance(self, words, word1, word2):
    # TODO: Write your code here
    idx1 = idx2 = -1
    res = float('inf')
    for i, word in enumerate(words):
      if word == word1: idx1 = i
      if word == word2: idx2 = i

      if idx1 != -1 and idx2 != -1:
        res = min(res, abs(idx1 - idx2))
    return res
