"""3924"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)  # 获取数列长度
        for i in range(lens):  # 进入循环
            for j in range(lens):
                if nums[i] + nums[j] == target:  # 判断和值是否为target
                    if i != j:  # 数组中同一个元素在答案里不能重复出现。
                        return [i, j]