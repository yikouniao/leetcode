# https://leetcode.com/problems/remove-element

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p1, p2 = n - 1, n - 1
        while p1 >= 0:
            if nums[p1] == val:
                nums[p1] = nums[p2]
                p2 -= 1
            p1 -= 1
        return p2 + 1


if __name__ == '__main__':
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))


