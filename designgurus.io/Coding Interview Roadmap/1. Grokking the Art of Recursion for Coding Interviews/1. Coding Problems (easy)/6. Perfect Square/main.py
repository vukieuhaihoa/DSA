class Solution:
  def sol(self, num, i):
    if i > num**0.5:
      return False
    return True if num == i*i else self.sol(num, i + 1)
  def isPerfectSquare(self, num):
    # TODO: Write your code here
    return self.sol(num, 1)