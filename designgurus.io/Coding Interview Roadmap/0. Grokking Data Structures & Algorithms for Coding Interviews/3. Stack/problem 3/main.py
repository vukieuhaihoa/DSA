import json

class Solution: 
    def decimalToBinary(self, num):
        # ToDo: Write Your Code Here.
        s = []
        while num:
            s.append(num % 2)
            num //= 2

        return ''.join(list(map(str, reversed(s)))) 

def read_test_case():
    text = input()
    # res = list(map(int, text.strip('][').split(',')))
    res = json.loads(text)
    return res

def main():
    test_case = read_test_case()
    sol = Solution()
    res = sol.decimalToBinary(test_case)
    print(res)

if __name__ == '__main__':
    main()