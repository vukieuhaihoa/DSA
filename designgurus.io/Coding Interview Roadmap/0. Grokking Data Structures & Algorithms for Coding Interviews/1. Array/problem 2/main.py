class Solution:
   def contains_duplicate(self, nums):
      # Approach 1: sort 
      # TC: O(n * log(n))
      # SP: O(1)
      # nums.sort()
      # for i in range(len(nums) - 1):
      #    if nums[i] == nums[i + 1]:
      #       return True
      
      # Approach 2: Set or Dict
      # TC: O(n)
      # SP: O(n) 
      s = set()
      for num in nums:
         if num in s:
            return True
         s.add(num)
      return False
   
def read_test_case():
   text = input()
   res = list(map(int, text.strip('][').split(',')))
   return res 

def main():
   test_case = read_test_case()
   sol = Solution()
   print(sol.contains_duplicate(test_case))

if __name__ == '__main__':
   main()