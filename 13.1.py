"""罗马数字转阿拉伯"""


class Solution:
    def romanToInt(self, s: str) -> int:
        thelist={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        last = None
        for c in s[::-1]:
            n = thelist[c]
            result += n if(n > result or last == c) else -n  # 逆序遍历后非正序的数组取负
            last = c
        return result