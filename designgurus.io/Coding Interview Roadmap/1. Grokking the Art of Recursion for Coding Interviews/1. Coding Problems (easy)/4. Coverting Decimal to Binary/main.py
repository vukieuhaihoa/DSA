class Solution:
  def decimalToBinary(self, decimal):        
    # TODO: Write your code here
    if decimal == 0:
      return ""
    
    return self.decimalToBinary(decimal // 2) + str(decimal % 2)
