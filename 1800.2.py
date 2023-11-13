class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = t = 0
        for i, v in enumerate(nums):
            if i == 0 or v > nums[i - 1]:
                t += v
            elif v <= nums[i - 1]:
                ans = max(ans, t)
                t = v
        ans = max(ans, t)
        return ans