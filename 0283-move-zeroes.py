# https://leetcode.com/problems/move-zeroes/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p, q = 0, 0
        while q < len(nums):
            if nums[q] != 0 and nums[p] == 0:
                nums[p] = nums[q]
                nums[q] = 0
                p += 1
            elif nums[p] != 0:
                p += 1
            q += 1
                

if __name__ == '__main__':
    nums = [1,0,1]
    Solution().moveZeroes(nums)
    print(nums)


