class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            i = left
            while i < right:
                if s[i] != s[right]:
                    i += 1
                else:
                    if right - left > max_len:
                        max_len = right - left
                    left = i + 1
                    break
            right += 1
        if max_len == 0:
            max_len = len(s)
        elif right - left > max_len:
            max_len = right - left
        return max_len
