import json

from collections import deque

class Solution:
    def checkPalindrome(self, s):
        # ToDo: Write Your Code Here.
        # s = s.replace(' ', '')
        # s = s.lower()
        # l = 0
        # r = len(s) - 1
        # while l <= r:
        #     if s[l] != s[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True
        q = deque()
        for ch in s.replace(' ', '').lower():
            q.append(ch)
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.checkPalindrome(test_case)
    print(res)
    
if __name__ == '__main__':
    main()