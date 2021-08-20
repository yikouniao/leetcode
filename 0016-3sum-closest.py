class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s > target:
                    k -= 1
                else:
                    j += 1
                if abs(s - target) < abs(res - target):
                    res = s
        return res
