class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        half = (n + m) // 2

        lo1, hi1 = -1, n - 1  # allow empty left partition in nums1

        while True:
            mid1 = (lo1 + hi1) // 2
            mid2 = half - mid1 - 2

            nums1Left  = nums1[mid1] if mid1 >= 0 else float('-inf')
            nums1Right = nums1[mid1 + 1] if (mid1 + 1) < n else float('inf')
            nums2Left  = nums2[mid2] if mid2 >= 0 else float('-inf')
            nums2Right = nums2[mid2 + 1] if (mid2 + 1) < m else float('inf')

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if (n + m) % 2:
                    return float(min(nums1Right, nums2Right))
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2

            elif nums1Left > nums2Right:
                hi1 = mid1 - 1
            else:
                lo1 = mid1 + 1