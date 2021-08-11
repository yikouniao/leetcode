class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        pi = 0
        r = 0
        for pj in range(n):
            if s[pj] in d:
                d[s[pj]] += 1 
            else:
                d[s[pj]] = 1
                
            while d[s[pj]] > 1:
                d[s[pi]] -= 1
                pi += 1
            
            r = max(r, pj - pi + 1)
        
        return r
