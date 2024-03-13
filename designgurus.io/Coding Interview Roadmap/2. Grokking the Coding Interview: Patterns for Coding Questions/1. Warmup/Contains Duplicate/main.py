import json


class Solution:
    def containsDuplicate(self, nums):
        # Approach 1: 
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Approach 2:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

        # Approach 3:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.containsDuplicate(test_case)
    print(res)

if __name__ == '__main__':
    main()