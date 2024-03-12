class Solution:
  def binarySearch(self, nums, target):
        # TODO: Write your code here
        if len(nums) == 0:
          return False
        mid = len(nums) // 2
        if nums[mid] == target:
          return True
        elif target > nums[mid]:
          return self.binarySearch(nums[mid+1:], target)  
        else:
          return self.binarySearch(nums[:mid], target)