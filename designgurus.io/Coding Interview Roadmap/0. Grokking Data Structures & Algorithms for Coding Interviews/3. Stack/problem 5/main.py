import json

class Solution:
    def sortStack(self,stack):
        tempStack = []
        
        # ToDo: Write Your Code Here.
        n = len(stack)
        for _ in range(len(stack)):
            # find the smallest element from stack using tempStack
            smallest = float('inf')
            count = 0
            if n == 0: 
                return stack
            for _ in range(n):
                ele = stack.pop()
                tempStack.append(ele)
                if ele < smallest:
                    smallest = ele
                    count = 1
                    continue
                if ele == smallest:
                    count += 1
                
            
            # current: stack = [], tempStack = [-1, -5, 10, 20], smallest = -5
            # push the number of smallest elements to stack
            # maybe -5 can appear 2 3 4 times
            for _ in range(count):
                stack.append(smallest)
                
            # stack = [-5], tempStack = [-1, -5, 10, 20], smallest = -5
            # stack = [-5], push all tempStack to stack without "smallest" ele
            for _ in range(len(tempStack)):
                ele = tempStack.pop()
                if ele != smallest:
                    stack.append(ele)
            # stack = [-5, 20, 10, -1], tempStack = [], smallest = -5     
            n -= count # n = 3
        
        return stack
    
def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.sortStack(test_case)
    print(res)

if __name__ == '__main__':
    main()