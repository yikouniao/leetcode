from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i, j, sum, result = 0, 0, 0, float('inf')
        while j < n:
            sum += nums[j]
            while sum >= target:
                result = min(result, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        return 0 if result > n else result

if __name__ == '__main__':
    list = [2,3,1,2,4,3]
    print(Solution().minSubArrayLen(7, list))
    print(list)