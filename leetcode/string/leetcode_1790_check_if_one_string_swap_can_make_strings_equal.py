# leetcode_1790_https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        differences:list[int] = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences.append(i)
        if len(differences) == 0:
            return True
        if len(differences) != 2:
            return False

        i: int
        j: int
        i, j = differences
        return s1[i] == s2[j] and s1[j] == s2[i]

