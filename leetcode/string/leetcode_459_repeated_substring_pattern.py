# leetcode_459_https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n: int = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substring: str = s[:i]
                if substring * (n//i) == s:
                    return True
        return False



