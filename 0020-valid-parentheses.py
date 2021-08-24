class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        t = []
        for c in s:
            if c in ('(', '[', '{'):
                t.append(c)
            else:
                if len(t) == 0:
                    return False
                m = t[-1]
                del t[-1]
                if (m == '(' and c == ')') or (m == '[' and c == ']') or (m == '{' and c == '}'):
                    continue
                else:
                    return False
        return False if len(t) > 0 else True
