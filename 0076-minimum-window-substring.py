from typing import *

class Solution:
    def minWindow(self, s: str, t: str) -> int:
        i, j = 0, 0
        count = len(t)
        result_len, result_i, result_j = len(s) + 1, 0, -1
        m = {}
        for c in t:
            m[c] = m.get(c, 0) + 1
        while j < len(s):
            if s[j] in m:
                if m[s[j]] > 0:
                    count -= 1
                m[s[j]] -= 1
            while count == 0:
                if j - i + 1 < result_len:
                    result_len, result_i, result_j = j - i + 1, i, j
                if s[i] in m:
                    if m[s[i]] == 0:
                        count += 1
                    m[s[i]] += 1
                i += 1
            j += 1
        return s[result_i:result_j + 1]

if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    print(Solution().minWindow("a", "a"))
    print(Solution().minWindow("a", "aa"))

