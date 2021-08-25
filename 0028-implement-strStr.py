class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n, m = len(needle), len(haystack)
        if n > m:
            return -1
        for i in range(m - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1
