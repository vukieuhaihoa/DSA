import json


class Solution:
  def reverseVowels(self, s: str) -> str:
    # TODO: Write your code here
    lst = list(s)
    l = 0
    r = len(lst) - 1
    vowels = 'ueoaiUEOAI'
    while l < r:
        while l < r and lst[l] not in vowels:
           l += 1
        while l < r and lst[r] not in vowels:
            r -= 1
        lst[l], lst[r] = lst[r], lst[l]
        l += 1
        r -= 1
    return ''.join(lst)

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.reverseVowels(test_case)
    print(res)

if __name__ == '__main__':
    main()