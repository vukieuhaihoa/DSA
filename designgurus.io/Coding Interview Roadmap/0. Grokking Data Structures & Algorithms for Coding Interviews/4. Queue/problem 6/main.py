import json
from collections import deque

class Solution:
    def printMax(self, arr, k):
        result = []
        # ToDo: Write Your Code Here.
        q = deque()
        
        # what's happened when k > len(arr)
        
        max_cur = float('-inf')
        for i in range(k):
            q.append(arr[i])
            if arr[i] > max_cur:
                max_cur = arr[i]
        result.append(max_cur)
        
        for i in range(k, len(arr)):
            q.popleft()
            q.append(arr[i])
            if arr[i] > max_cur:
                max_cur = arr[i]
            result.append(max_cur)
        
        return result


def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    arr = json.loads(text)
    text = input()
    k = json.loads(text)
    return arr, k

def main():
    arr, k = read_test_case()
    sol = Solution()
    res = sol.printMax(arr, k)
    print(res)

if __name__ == '__main__':
    main()