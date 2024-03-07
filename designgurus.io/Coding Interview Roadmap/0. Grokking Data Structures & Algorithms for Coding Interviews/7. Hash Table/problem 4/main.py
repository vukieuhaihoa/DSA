from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:      
        length = 0
        # ToDo: Write Your Code Here.        
        freq_map = Counter(s)
        
        odd_found = False
        for k, v in freq_map.items():
            if v & 1:
                odd_found = True
                length += v - 1
            else:
                length += v
        return length + 1 if odd_found else length 

        """Thought Process
        tại vì một s là một palindrome thì có hai trường hợp:
        + độ dài là một số chẵn
        + độ dài là một số lẽ 
        Nếu chia đôi s ra:
        + len - chẵn: ví dụ: abc|cba 
        + len - lẽ: ví dụ pepe[a]epep
        giải thuật ở đây là mình build một map để đếm số lần suất hiện của mỗi ký tự ví dụ chuỗi ban đầu là 'bananas'
        map sau khi build {
            'b': 1,
            'a': 3,
            'n': 2,
            's': 1
        }
        
        - nếu một ký tự suất hiện chẵn lần thì nó có thể phân bổ đều hai bên 
        => mình cộng dồn số lần xh vào length luôn
        - nếu một ký tự suất hiện lẽ lần, mình trừ nó đi một => rồi cộng dồn vào length
        Question: Tại sao phải trừ một ?
        Answer: Tại vì một ký tự này có thể nằm chính giữa trong str có độ dài lẽ => mình sẽ tạo một biến cờ 'odd_found' để check xem có kí tự nào xh lẽ lần không
        Sau khi kết thúc vòng lặp mình sẽ kiểm tra biến 'odd_found' để cộng thêm một vào length.
        """