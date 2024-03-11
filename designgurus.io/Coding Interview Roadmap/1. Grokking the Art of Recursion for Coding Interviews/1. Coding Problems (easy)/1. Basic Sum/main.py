class Solution:
  def calculateSum(self, N):
    # TODO: Write your code here
    if N == 0:
      return N

    return N + self.calculateSum(N - 1);