
from typing import *

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a, b = -1, -1
        result, curr_result, count_b = 0, 0, 0
        for fruit in fruits:
            if fruit != a and fruit != b:
                curr_result = count_b + 1
                result = max(result, curr_result)
                count_b = 1
                a, b = b, fruit
            elif fruit == b:
                curr_result += 1
                result = max(result, curr_result)
                count_b += 1
            else:
                curr_result += 1
                result = max(result, curr_result)
                count_b = 1
                a, b = b, a      
        return result

if __name__ == '__main__':
    list = [3,3,3,1,2,1,1,2,3,3,4]
    print(Solution().totalFruit(list))
    print(list)
