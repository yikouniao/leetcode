import re
from typing import *
from unittest import result

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 2:
            return n
        i, j = 0, 0
        result = j - i + 1
        a, b = fruits[0], fruits[0]
        count_b = 1
        j += 1
        while j < n:
            if fruits[j] == b:
                count_b += 1
                result = max(result, j - i + 1)
                j += 1
            elif fruits[j] == a:
                count_b = 1
                a = b
                b = fruits[j]
                result = max(result, j - i + 1)
                j += 1
            elif a != b:
                i = j - count_b
                result = max(result, count_b + 1)
                count_b = 1
                a = b
                b = fruits[j]
                j += 1
            else:
                result = max(result, j - i + 1)
                count_b = 1
                b = fruits[j]
                j += 1
        return result

if __name__ == '__main__':
    list = [0,1,2,2]
    print(Solution().totalFruit(list))
    print(list)
