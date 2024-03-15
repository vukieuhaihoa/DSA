class Solution:
  def isAnagram(self, s, t):
    # TODO: Write your code here
    d = {}
    if len(s) != len(t):
      return False

    for i in range(len(s)):
      d[s[i]] = d[s[i]] + 1 if s[i] in d else 1
      d[t[i]] = d[t[i]] - 1 if t[i] in d else -1
      
      if s[i] in d and d[s[i]] == 0: del d[s[i]]
      if t[i] in d and d[t[i]] == 0: del d[t[i]]
      
    return not d