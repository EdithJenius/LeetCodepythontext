"""2252 13.7"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens-1):
            for j in range(i+1, lens):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]