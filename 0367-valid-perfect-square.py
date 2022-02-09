# https://leetcode.com/problems/valid-perfect-square

from typing import List

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + int((right - left) / 2)
            if mid == num / mid:
                return True
            elif mid > num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    print(Solution().isPerfectSquare(10))


