# https://leetcode.com/problems/remove-element

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i] = nums[j]
                nums[j] = val
                j -= 1
                i += 1
            else:
                i += 1
        return j + 1
        
        


if __name__ == '__main__':
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))


