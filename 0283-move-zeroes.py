# https://leetcode.com/problems/move-zeroes/

from typing import List

class Solution:
    def moveZeors(self, nums: List[int]) -> None:
        p, q = 0, 1
        while q < len(nums):
            if nums[q] == 0:
                q += 1
            elif nums[p] == 0:
                nums[p] = nums[q]
                nums[q] = 0
                q += 1
                p += 1
            else:
                q += 1
                p += 1
                
                
        
        


if __name__ == '__main__':
    nums = [0,1,2,2,0,0,0,3,3,4,5]
    Solution().moveZeors(nums)
    print(nums)


