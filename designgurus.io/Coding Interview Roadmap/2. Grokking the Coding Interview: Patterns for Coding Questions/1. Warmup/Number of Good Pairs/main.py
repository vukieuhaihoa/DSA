class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0
    # TODO: Write your code here
    d = {}
    for num in nums:
      if num in d:
        d[num] += 1
        pairCount += d[num] - 1
      else:
        d[num] = 1
    return pairCount
