import json

class Solution:
    def maximumWealth(self,accounts):
        max_wealth = 0

        for acc in accounts:
            total = sum(acc)
            if total > max_wealth:
                max_wealth = total
                
        return max_wealth

def read_test_case():
    text = input()
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.maximumWealth(test_case)
    print(res)

if __name__ == '__main__':
    main()