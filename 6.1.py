"""56 15.1"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s  # 大于三行时执行变换
        res = ["" for _ in range(numRows)]  # 生成一个元素为5个空字符的str格式
        i, flag = 0, -1
        for c in s:
            res[i] += c  # 把c填入对应行中
            if i == 0 or i == numRows - 1: flag = -flag # 当到达Z的转折点是将flag取反
            i += flag
        return "".join(res)
