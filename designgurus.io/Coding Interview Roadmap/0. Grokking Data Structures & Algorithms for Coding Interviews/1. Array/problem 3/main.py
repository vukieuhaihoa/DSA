class Solution:
    def findDifferenceArray(self, nums):
        # Approach 1: prefix sum
        # TC: O(3*n)
        # SP: O(3*n)
        # n = len(nums)
        # left_sum = [0] * n
        # right_sum = [0] * n

        # # build left sum
        # left_sum[0] = nums[0]
        # for i in range(1, n):
        #     left_sum[i] = left_sum[i - 1] + nums[i]
        
        # # build right sum
        # right_sum[n - 1] = nums[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_sum[i] = right_sum[i + 1] + nums[i]

        # ans = [0] * n
        # for i in range(n):
        #     ans[i] = abs(right_sum[i] - left_sum[i])
        
        # return ans
        
        
        # Approach 2: Optimize prefix sum
        n = len(nums)
        # build prefix_sum
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        ans = [0] * len(nums)
        for i in range(n):
            left_sum = 0
            right_sum = 0
            
            if i == 0:
                left_sum = 0
            else:
                left_sum = prefix_sum[i - 1]
                
            if i == n - 1:
                right_sum = 0
            else:
                right_sum = prefix_sum[-1] - prefix_sum[i]        
            
            ans[i] = abs(left_sum - right_sum)        
        return ans

def read_test_case():
    text = input()
    res = list(map(int, text.strip('][').split(',')))
    return res 

def main():
    test_case = read_test_case()
    sol = Solution()
    print(sol.findDifferenceArray(test_case))

if __name__ == '__main__':
    main()

# 2, 5, 1, 6

# prefix sum:
# 2, 7, 8, 14

# at indice 0:
# => right_sum = 14 - 2 = prefix_sum[-1] - prefix_sum[0]
# => left_sum = 0
# =>> 12

# at indice 1:
# => right_sum = 14 - 7 = prefix_sum[-1] - prefix_sum[1]
# => left_sum = prefix_sum[i - 1] = prefix_sum[0] = 2
# =>> 7 - 2 = 5 