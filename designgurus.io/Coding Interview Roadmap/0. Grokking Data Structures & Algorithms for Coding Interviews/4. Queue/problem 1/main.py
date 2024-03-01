import json

class Solution:
    def reverseQueue(self, queue):
        # ToDo: Write Your Code Here.
        stack = []
        while queue:
            stack.append(queue.pop(0))
        while stack:
            queue.append(stack.pop())

        return queue

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.reverseQueue(test_case)
    print(res)

if __name__ == '__main__':
    main()