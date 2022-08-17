"""1884"""
"""枚举"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            for j in range(i, lens):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]