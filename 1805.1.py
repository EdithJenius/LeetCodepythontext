‘错误’

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        n = len(word)
        num = 0
        nums = []
        ans = 0
        for i in range(n):
            if 48 <= ord(word[i]) and ord(word[i]) <= 57:
                num = num * 10 + int(word[i])
                if i == n:
                    if str(num) not in nums:
                        nums.append(str(num))
            else:
                if str(num) not in nums:
                    nums.append(str(num))
                num = 0

        if "0" in word:
            ans += 1
        else:
            ans = len(nums) - 1
        return ans