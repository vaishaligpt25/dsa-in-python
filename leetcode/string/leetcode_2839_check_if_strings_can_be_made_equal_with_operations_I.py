# leetcode_2839_https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check characters at even indices(0, 2)
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
        # Check characters at odd indices(1,3)
        if sorted([s1[1], s1[3]]) != sorted([s2[1],s2[3]]):
            return False

        return True


    def canBeEqual1(self, s1: str, s2: str) -> bool:
        return set(s1[0] + s1[2]) == set(s2[0] + s2[2]) and \
               set(s1[1] + s1[3]) == set(s2[1] + s2[3])



    def canBeEqual2(self, s1: str, s2: str) -> bool:
            # Check if strings are already equal
            if s1 == s2:
                return True

            # Check if swapping positions 0 and 2 makes strings equal
            if s1[2] + s1[1] + s1[0] + s1[3] == s2:
                return True

            # Check if swapping positions 1 and 3 makes strings equal
            if s1[0] + s1[3] + s1[2] + s1[1] == s2:
                return True

            # Check if both swaps are needed
            if s1[2] + s1[3] + s1[0] + s1[1] == s2:
                return True

            return False





