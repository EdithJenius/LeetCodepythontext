"""超时"""


class Solution(object):
    def longestPalindrome(self,s):
        max = 0
        l = ''
        t = s[0]
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                l = s[i:j]
                if l == l[::-1]:
                    n = j - i
                    if n>max:
                        max = n
                        t = l
        return t