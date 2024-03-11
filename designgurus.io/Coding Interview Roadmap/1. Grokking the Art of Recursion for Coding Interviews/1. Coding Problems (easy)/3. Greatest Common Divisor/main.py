class Solution:
  def calculateGCD(self, A, B):
    # TODO: Write your code here
    if B == 0:
      return A
    return self.calculateGCD(B, A%B)