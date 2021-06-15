class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return True if int(str(abs(x))[::-1]) == x else False