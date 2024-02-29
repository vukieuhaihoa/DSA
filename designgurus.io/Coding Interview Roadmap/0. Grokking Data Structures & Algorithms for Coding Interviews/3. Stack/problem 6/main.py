import json

class Solution:
    def simplifyPath(self, path):
        # ToDo: Write Your Code Here.
        stack = []
        for p in path.split('/'):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        
        return '/' + '/'.join(stack)

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.simplifyPath(test_case)
    print(res)

if __name__ == '__main__':
    main()