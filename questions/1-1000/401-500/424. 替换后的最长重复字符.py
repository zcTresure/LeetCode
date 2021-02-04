# Date:       2021/2/4
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left


test = Solution()
s = "ABAB"
k = 2
print(test.characterReplacement(s, k))
