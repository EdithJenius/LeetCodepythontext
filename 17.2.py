class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
                for letter in phone[ord(digit)-50]:  # ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr()
                    # 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的
                    # Python 定义范围，则会引发一个 TypeError 的异常。
                    queue.append(tmp + letter)  # append() 方法用于在列表末尾添加新的对象。
        return queue