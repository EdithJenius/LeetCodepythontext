"""整数转罗马数字"""


class Solution:
    def intToRoman(self, num: int) -> str:
        # 用整除和趋于来确定符号以及符号数量
        # 确定是否为4和9的10^倍
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I'}
        # 哈希表
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key
                res += hashmap[key] * count
                num %= key
        return res
