# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, q = 0, 1
        while q < len(nums):
            if nums[p] == nums[q]:
                q += 1
            else:
                nums[p + 1] = nums[q]
                q += 1
                p += 1
        return p + 1
        


if __name__ == '__main__':
    print(Solution().removeDuplicates([0,1,2,2,3,3,4,5]))


