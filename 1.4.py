"""哈希"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasht = dict()  # 创建哈希表
        for i in range(len(nums)):
            if target - nums[i] in hasht:
                return [hasht[target - nums[i]], i]
            hasht[nums[i]] = i
        return []
