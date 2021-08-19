class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        while i < len(strs[0]):
            t = strs[0][i]
            for string in strs:
                if i < len(string) and t == string[i]:
                    continue
                else:
                    return strs[0][0:i]
            i += 1
        
        return strs[0][0:i]
