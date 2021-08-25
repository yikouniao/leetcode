class Solution:
    def generateParenthesis(self, n):
        table = [[] for _ in range(n + 1)]
        table[0].append('')
        for i in range(1, n + 1):
            for j in range(i):
                table[i] += ['(' + a + ')' + b for a in table[j] for b in table[i - j - 1]]
        return table[n]
