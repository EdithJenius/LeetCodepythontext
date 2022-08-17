class Solution:
    def reverse(self, x: int) -> int:
        rev_num = int(str(abs(x))[::-1])
        x_rev = rev_num if x >= 0 else (-1)*rev_num
        if -2**31 <= x_rev <= 2**31 - 1:  # 数字与运算之间，数字的内存消耗更小，但执行时间更长
            return x_rev
        return 0