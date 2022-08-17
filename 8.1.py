"""请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）"""
"""不知道哪里错了"""

class Solution:
    def myAtoi(self, s: str) -> int:
        l = len(s)
        t = ""
        n = 1
        x = 0
        for i in range(l):
            if 0 <= int(float(s[i])) <= 9:
                t = t + s[i]
            elif s[i] == "-":
                n *= -1
        t = int(t)
        x = t*n
        return x


