class Solution:
  def calculateFactorial(self, number):
    # TODO: Write your code here
    if number <= 1:
      return 1
    return number * self.calculateFactorial(number - 1)