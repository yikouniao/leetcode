class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        r = 0
        while i < j:
            if height[i] < height[j]:
                r = max(r, (j - i) * height[i])
                i += 1
            elif height[i] > height[j]:
                r = max(r, (j - i) * height[j])
                j -= 1
            else:
                r = max(r, (j - i) * height[i])
                i += 1
                j -= 1
        return r
