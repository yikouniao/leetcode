from typing import *

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        ps, pt = ns - 1, nt - 1
        skip_s, skip_t = 0, 0
        while ps >= 0 or pt >= 0:
            while ps >= 0:
                if s[ps] == "#":
                    skip_s += 1
                elif skip_s > 0:
                    skip_s -= 1
                else:
                    break
                ps -= 1
            while pt >= 0:
                if t[pt] == "#":
                    skip_t += 1
                elif skip_t > 0:
                    skip_t -= 1
                else:
                    break
                pt -= 1
            if ps >= 0 and pt >= 0 and s[ps] != t[pt]:
                return False
            if (ps < 0 and pt >= 0) or (ps >= 0 and pt < 0):
                return False
            ps -= 1
            pt -= 1
        return True

if __name__ == '__main__':
    s, t = "ab#c", "ad#c"
    print(Solution().backspaceCompare(s, t))
    
