class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        p, q = 0, 0
        while q < n:
            while q < n and nums[q] == val:
                q += 1
            if q < n:
                nums[p] = nums[q]
                q += 1
                p += 1
        return p
