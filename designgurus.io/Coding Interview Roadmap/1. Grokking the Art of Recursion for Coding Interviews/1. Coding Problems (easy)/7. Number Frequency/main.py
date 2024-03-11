class Solution:
  def sol(self, arr, key, i):
    if i < 0:
      return 0
    return 1 + self.sol(arr, key, i - 1) if arr[i] == key else self.sol(arr, key, i - 1)

  def countOccurrences(self, arr, key):
    # TODO: Write your code here
    return self.sol(arr, key, len(arr) - 1)