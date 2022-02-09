# https://leetcode.com/problems/sqrtx

from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = left + int((right - left) / 2)
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1


if __name__ == '__main__':
    print(Solution().mySqrt(3))


