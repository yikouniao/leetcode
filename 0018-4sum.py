class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        res = []
        
        
        for i in range(0, n - 3):
            i_has_large, i_has_less, i_has_equal = False, False, False
            for l in range(n - 1, 2, -1):
                j, k = i + 1, l - 1
                j_has_large, j_has_less, j_has_equal = False, False, False
                while i < j and j < k and k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        if [nums[i], nums[j], nums[k], nums[l]] not in res:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                        j += 1
                        k -= 1
                        i_has_equal = True
                        j_has_equal = True
                    elif sum > target:
                        k -= 1
                        i_has_large = True
                        j_has_large = True
                    else:
                        j += 1
                        i_has_less = True
                        j_has_less = True
                if j_has_less and not j_has_equal and not j_has_large:
                    break
            if i_has_large and not i_has_equal and not i_has_less:
                break
        
        return res
