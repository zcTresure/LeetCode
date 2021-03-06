# -*- coding: utf-8 -*-
# File:      274. H 指数.py
# DATA:      2021/7/11
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h, i = 0, len(citations) - 1
        while i >= 0 and citations[i] >= h:
            h += 1
            i -= 1
        return h

    def hIndex(self, citations: List[int]) -> int:
        n, total = len(citations), 0
        counter = [0] * (n + 1)
        for i in range(n):
            if citations[i] >= n:
                counter[n] += 1
            else:
                counter[citations[i]] += 1
        for i in range(n, -1, -1):
            total += counter[i]
            if total >= i:
                return i
        return 0


citations = [3, 0, 1, 6, 5]
print(Solution().hIndex(citations))
