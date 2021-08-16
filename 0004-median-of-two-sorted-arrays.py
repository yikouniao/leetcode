class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i, j = 0, 0
        n = len(nums1) + len(nums2)
        while i < len(nums1) and j < len(nums2) and len(nums3) <= int(n / 2) + 1:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1
        
        if n == 0:
            return 0
        elif n % 2 == 1:
            return nums3[int(n / 2 - 0.5)]
        else:
            return (nums3[int(n / 2 - 1)] + nums3[int(n / 2)]) / 2
