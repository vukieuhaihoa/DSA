import json

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False
    
    def pop(self):
        if self.isEmpty():
            return None
        
        return self.stack.pop()    

    def peek(self):
        if self.isEmpty():
            return None
        
        return self.stack[-1]
    
class Solution:
    def isValid(self, str):
        # build stack
        s = Stack()
        
        for ch in str:
            if ch in [")", "}", "]"]:
                if ch == ")" and s.pop() != "(":
                    return False
                
                if ch == "]" and s.pop() != "[":
                    return False
                
                if ch == "}" and s.pop() != "{":
                    return False
            else:
                s.push(ch)
        
        # Edge case: "[", "{"
        return s.isEmpty()

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.isValid(test_case)
    print(res)

if __name__ == '__main__':
    main()