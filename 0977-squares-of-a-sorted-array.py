from typing import *

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mid = n - 1
        for i in range(1, n):
            if abs(nums[i]) > abs(nums[i - 1]):
                mid = i - 1
                break
        p, q = mid - 1, mid + 1
        result = [nums[mid] * nums[mid]]
        while p >= 0 and q < n:
            if abs(nums[p]) < abs(nums[q]):
                result.append(nums[p] * nums[p])
                p -= 1
            else:
                result.append(nums[q] * nums[q])
                q += 1
        while p >= 0:
            result.append(nums[p] * nums[p])
            p -= 1
        while q < n:
            result.append(nums[q] * nums[q])
            q += 1
        return result

if __name__ == '__main__':
    list = [-4,-1,0,3,10]
    print(Solution().sortedSquares(list))
    print(list)
