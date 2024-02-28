import json

class Solution:
    def findMaxOnesRow(self, mat):
        index = 0
        maximum = 0
        
        for i in range(len(mat)):
            total = sum(mat[i])
            if total > maximum:
                maximum = total
                index = i
        
        return [index, maximum] 
            
def read_test_case():
    text = input()
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.findMaxOnesRow(test_case)
    print(res)
    
if __name__ == '__main__':
    main()