from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n):
            # Skip duplicate 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the fixed number is > 0, remaining are >= it, so sum can't be 0
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # Move past duplicates for l and r
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
