import json
from collections import deque

class Solution:
    def printMax(self, arr, k):
        result = []
        # ToDo: Write Your Code Here.
        # what's happened when k > len(arr)
        dq = deque()
        n = len(arr)
        for i in range(min(k, n)):
            # Note: thằng lớn nhất nằm ở cuối window thì những thằng đầu bị xoá 
            # với mỗi phần tử, nếu phần tử trước nó nhỏ hơn phần tử hiện tại
            # thì những phần tử nhỏ hơn này nó sẽ trở nên vô dụng, vì sao ?
            # vì mình đang tìm phần tử lớn nhất trong k thằng mà, nếu thằng lớn 
            # lớn hơn nó nằm ở đằng sau thì không việc thì phải push index của 
            # những thằng nhỏ hơn vào deque làm gì 
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        for i in range(k, n):
            # the element at the front of the deque is the index of the element
            # of the previous window
            result.append(arr[dq[0]])
            
            # Remove the elements which are out of this window that have size k
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove all element at the end(rear) of the deque that smaller 
            # than the currently being added 
            # Remove useless elements
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            
            # at the index of the current element to the rear of the dq
            dq.append(i)
        
        # Element at the front of the deque is the largest element of the last window
        result.append(arr[dq[0]])
        return result       
        # Cách này sai quá sai
        # Giả sử giá trị lớn nhất của q nó nằm ở đầu của q thì sau khi mình 
        # nhích lên 1 phần tử
        # Input: [11, 10, 9, 8, 7, 6]  k = 3
        # Output: [11, 10, 8, 7]
        # nếu bằng cách này, thì max_cur = 11 [11, 10, 9]
        # bước vào sliding window thì khi bước vào phần tử 8 thì mình sẽ bỏ phân
        # tử 11: [10, 9 ,8], max_cur = 11 => cách này sai quá sai á
        # q = deque()
        # max_cur = float('-inf')
        # for i in range(k):
        #     q.append(arr[i])
        #     if arr[i] > max_cur:
        #         max_cur = arr[i]
        # result.append(max_cur)
        
        # for i in range(k, len(arr)):
        #     q.popleft()
        #     q.append(arr[i])
        #     if arr[i] > max_cur:
        #         max_cur = arr[i]
        #     result.append(max_cur)
        # return result


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