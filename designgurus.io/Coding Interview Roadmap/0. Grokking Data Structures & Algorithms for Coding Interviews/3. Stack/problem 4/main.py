import json

class Solution:
    def nextLargerElement(self, arr):
        res = [-1]*len(arr)
        # ToDo: Write Your Code Here.
        
        # TC: O(n^2)
        # for i in range(len(arr) - 1):
        #     for j in range(i + 1, len(arr)):
        #         if arr[j] > arr[i]:
        #             res[i] = arr[j]
        #             break
        st = []
        for i in range(len(arr) - 1, -1, -1):
            while st and st[-1] <= arr[i]:
                st.pop()
                
            if st:
                res[i] = st[-1]                    
            st.append(arr[i])
               
        return res

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.nextLargerElement(test_case)
    print(res)

if __name__ == '__main__':
    main()