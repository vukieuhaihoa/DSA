class Solution:
  def checkIfPangram(self, sentence):
    # TODO: Write your code here
    s = set()
    for ch in sentence.lower():
      if ch.isalpha():
        s.add(ch)
    return len(s) == 26