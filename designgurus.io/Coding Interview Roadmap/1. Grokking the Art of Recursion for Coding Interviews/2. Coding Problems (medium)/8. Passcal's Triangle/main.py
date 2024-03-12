class Solution:
  def generatePascalTriangle(self, numRows):
      triangle = []
      # TODO: Write your code here
      if numRows == 0:
          return []
      if numRows == 1:
          return [[1]]
      
      triangle = self.generatePascalTriangle(numRows - 1)
      prev_row = triangle[-1]
      cur_row = [1] * numRows
      for i in range(1, numRows - 1):
          cur_row[i] = prev_row[i] + prev_row[i - 1]
      triangle.append(cur_row)
      
      return triangle 

# Approach 2: Recursion by my self
# class Solution:
#   def sol(self, cur_row, target_row, lst):
#     if cur_row == target_row:
#       return lst
    
#     arr = [1] * (cur_row + 1)
#     for i in range(1, cur_row):
#       arr[i] = lst[cur_row - 1][i] + lst[cur_row - 1][i - 1]
#     lst.append(arr)
#     return self.sol(cur_row + 1, target_row, lst)

#   def generatePascalTriangle(self, numRows):
#       triangle = []
#       # TODO: Write your code here
#       return self.sol(0, numRows, triangle)



# Approach 1: Iterative
# class Solution:
#   def generatePascalTriangle(self, numRows):
#       triangle = []
#       # TODO: Write your code here
#       for i in range(numRows): # 0 1 2
#         triangle.append([1]*(i + 1))
#         for j in range(1, i):
#           triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#       return triangle