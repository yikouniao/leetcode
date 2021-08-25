class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        p, q = 0, 1
        while q < n:
            while q < n and nums[p] == nums[q]:
                q += 1
            if p + 1 < n and q < n:
                nums[p + 1] = nums[q]
                p += 1
                q += 1
        return p + 1  
