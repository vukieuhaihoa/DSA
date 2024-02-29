import json

class Solution:
    def removeStars(self, s):
        # ToDo: Write Your Code Here.
        st = []
        for ch in s:
            if ch != "*":
                st.append(ch)
            else:
                if st:
                    st.pop()
        
        
        return ''.join(st)

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.removeStars(test_case)
    print(res)
    
if __name__ == '__main__':
    main()