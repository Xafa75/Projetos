'''Given an integer x, return true if x is a 
palindrome, and false otherwise.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        reversedX = ''.join(reversed(str(x)))
        if str(reversedX) == str(x):
            return True
        else:
            return False
        