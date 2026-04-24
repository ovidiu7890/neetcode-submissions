class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(c.lower() for c in s if c.isalnum())
        n = len(s1)
        m = n//2
        i = 0
        while i<m:
            if s1[i] != s1[n-i-1]:
                return False
            i+=1
        return True
        