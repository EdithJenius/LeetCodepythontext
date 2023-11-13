class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = 0
        for i in range(n - k + 1):
            flag = True
            n1 = nums[0 + i:k + i - 1]
            set_n1 = set(n1)
            if len(set_n1) != len(n1):
                flag = False
            if flag is True:
                ans = sum(n1)
                flag = True
                if ans > mx:
                    mx = ans
                    ans = 0
        return mx

