class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s

        d = [[] for _ in range(numRows)]        
        
        for i in range(len(s)):
            mod = i % (2 * numRows - 2)
            row = mod if mod < numRows else 2 * numRows - mod - 2
            d[row].append(s[i])
        r = ''.join([''.join(t) for t in d])
        return r
