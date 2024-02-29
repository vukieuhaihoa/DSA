import json

class Solution:
    def removeDuplicates(self, s):
        st = []
        
        for ch in s:
            if st and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
        
        return ''.join(st)

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.removeDuplicates(test_case)
    print(res)

if __name__ == '__main__':
    main()