# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p1, p2 = 0, 1
        while p2 < n:
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1


if __name__ == '__main__':
    print(Solution().removeDuplicates([0,1,2,2,3,3,4,5]))


