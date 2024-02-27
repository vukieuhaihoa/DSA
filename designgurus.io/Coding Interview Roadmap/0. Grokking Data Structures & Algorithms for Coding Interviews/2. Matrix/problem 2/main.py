import json

class Solution:
    def diagonalSum(self, mat):
        res = 0
        if len(mat) != len(mat[0]):
            return res
        n = len(mat)
        for i in range(n):
           res += mat[i][i] + mat[i][n - 1 - i] 

        if n & 1:
            return res - mat[n//2][n//2] 
        return res
    
    
def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.diagonalSum(test_case)
    print(res)

if __name__ == '__main__':
    main()