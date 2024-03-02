import json
from queue import Queue

class Solution:
    def generateBinaryNumbers(self, n):
        res = []
        # ToDo: Write Your Code Here.
        q = Queue()
        q.put("1")
        for _ in range(0, n):
            if q:
                top = q.get()
                q.put(top + "0")
                q.put(top + "1")
                res.append(top)                 
        return res

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.generateBinaryNumbers(test_case)
    print(res)

if __name__ == '__main__':
    main()