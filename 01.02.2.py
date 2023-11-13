class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        dic = defaultdict(int)
        for n in s1:
            dic[n] += 1
        for n in s2:
            dic[n] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True