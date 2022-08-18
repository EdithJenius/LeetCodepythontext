from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        n = len(nums)
        best = 10 ** 7  # 把best设为无穷大

        def update(cur):
            nonlocal best  # 非局部声明变量指代的已有标识符是最近外面函数的已声明变量，但是不包括全局变量。
            if abs(cur - target) < abs(best - target):  # 判断是否为最接近target的值
                best = cur

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # 相同元素跳过
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:  # 找到下一个不同于k的值
                        k0 -= 1
                    k = k0
                else:
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:  # 找到下一个不同于j的值
                        j0 += 1
                    j = j0
        return best
