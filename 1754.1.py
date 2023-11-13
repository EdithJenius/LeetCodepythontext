class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        t = 0
        merge = ""
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                t += 1
            else:
                break
        merge = word1[:t]
        word1 = word1[t:]
        word2 = word2[t:]

        while word1 or word2:
            if word1 and (not word2 or word1[0] >= word2[0]):
                merge += word1[0]
                word1 = word1[1:]
            else:
                merge += word2[0]
                word2 = word2[1:]
        return merge