class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se={}
        for c in s:
            if c in se:
                se[c] += 1
            else:
                se[c] = 1
        for c in t:
            if c in se:
                if se[c] <= 0:
                    return False
                else:
                    se[c] -= 1
            else:
                return False
        return True
        