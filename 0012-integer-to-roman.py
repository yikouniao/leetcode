class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        r = ""
        for v, n in zip(values, numerals):
            r += n * (num // v)
            num %= v
            if num == 0:
                break
        
        return r
