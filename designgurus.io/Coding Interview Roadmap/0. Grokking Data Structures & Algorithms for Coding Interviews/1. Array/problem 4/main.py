class Solution:
    def largestAltitude(self, gain):
        res = 0
        if gain[0] > res:
            res = gain[0]
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            if gain[i] > res:
                res = gain[i]         
        return res

def read_test_case():
    text = input()
    res = list(map(int, text.strip('][').split(',')))
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.largestAltitude(test_case)
    print(res)

if __name__ == '__main__':
    main()