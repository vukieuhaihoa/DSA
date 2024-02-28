import json

class Solution:
    def reverseString(self, s):
        # ToDo: Write Your Code Here.
        st = []
        res = ""
        
        for ch in s:
            st.append(ch)    
        
        while st: 
            res += st.pop()
        return res
    
def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.reverseString(test_case)
    print(res)

if __name__ == '__main__':
    main()