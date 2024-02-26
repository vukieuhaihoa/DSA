
class Solution:
    def running_sum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def read_test_case():
    text = input()
    res = list(map(int, text.strip('][').split(',')))
    return res


def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.running_sum(test_case)
    print(res)
    

if __name__ == '__main__':
    main()