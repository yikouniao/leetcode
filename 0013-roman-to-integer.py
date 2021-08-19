
class Solution:
    def romanToInt(self, s: str) -> int:
        # values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        m = {
            "M": 1000,
            "CM": 900, 
            "D": 500, 
            "CD": 400, 
            "C": 100, 
            "XC": 90, 
            "L": 50, 
            "XL": 40, 
            "X": 10, 
            "IX": 9, 
            "V": 5, 
            "IV": 4, 
            "I": 1
        }
        
        r = 0
        
        n = len(s)
        i = 0
        while i < n:
            t = 0
            if i < n - 1:
                t = m.get(s[i:i+2], 0)
            if t > 0:
                r += t
                i += 2
            else:
                r += m.get(s[i], 0)
                i += 1

        
        return r
