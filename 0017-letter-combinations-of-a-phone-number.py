class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        d = {}
        d['2'] = {'a','b','c'}
        d['3'] = {'d','e','f'}
        d['4'] = {'g','h','i'}
        d['5'] = {'j','k','l'}
        d['6'] = {'m','n','o'}
        d['7'] = {'p','q','r','s'}
        d['8'] = {'t','u','v'}
        d['9'] = {'w','x','y','z'}
        
        res = [""]
        for c in digits:
            res = [[r + cc for cc in d[c]] for r in res]
            res = [rr for r in res for rr in r]
                
        return res
