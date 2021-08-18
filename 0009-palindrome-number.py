class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        a = x
        r = 0
        while a != 0:
            r = r * 10 + a % 10
            a //= 10
        return r == x
