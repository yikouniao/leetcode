class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        a = [[False] * n for _ in range(n)]
        r = s[0]
        for i in range(n):
            a[i][i] = True
        for l in range(2, n + 1):
            for i in range(n - 1):
                if i + l - 1 < n and s[i] == s[i + l - 1] and (l == 2 or a[i + 1][i + l - 2]):
                    a[i][i + l - 1] = True
                    r = s[i : i + l]

        return r
