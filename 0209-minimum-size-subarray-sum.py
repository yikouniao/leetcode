import re
from typing import *
from unittest import result

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = n + 1
        if n == 0:
            return result
        i, j, sum = 0, 0, nums[0]
        while i < n:
            if sum >= target:
                result = min(result, j - i + 1)
                sum -= nums[i]
                i += 1
            elif j == n - 1:
                break
            else:
                j += 1
                sum += nums[j]
        return 0 if result > n else result

if __name__ == '__main__':
    list = [2,3,1,2,4,3]
    print(Solution().minSubArrayLen(7, list))
    print(list)
