from typing import *

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        i, j = 0, n - 1
        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i] * nums[i]
                i += 1
            else:
                result[k] = nums[j] * nums[j]
                j -= 1
        return result
    
if __name__ == '__main__':
    list = [-4,-1,0,3,10]
    print(Solution().sortedSquares(list))
    print(list)
