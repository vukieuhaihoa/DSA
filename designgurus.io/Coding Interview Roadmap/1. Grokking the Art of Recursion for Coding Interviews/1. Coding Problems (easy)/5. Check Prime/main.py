class Solution:
  def __checkPrime(self, n, i):
    if i > n ** 0.5:   
      return True
    if n % i == 0:
      return False
    return self.__checkPrime(n, i + 1)
  def isPrime(self, number):
    # TODO: Write your code here
    if number < 2:
      return False
    if number == 2:
      return True
    return self.__checkPrime(number, 2)