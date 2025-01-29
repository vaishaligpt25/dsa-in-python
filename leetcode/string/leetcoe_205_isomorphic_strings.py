# leetcode_205:-https://leetcode.com/problems/isomorphic-strings/description/?envType=problem-list-v2&envId=string

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # map to keep track of character mappings
        s_to_t = {}  #map s chars to t chars
        t_to_s = {}  #map t chars to s chars

        for c1, c2 in zip(s, t):
            # three cases to handle:
            # 1. c1 is already mapped
            # 2. c2 is already mapped
            # 3. neither is mapped

            #if c1 seen before, it should map to same character
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False

            #if c1 is not seen before but c2 is mapped to different character
            elif c2 in t_to_s:
                return False

            #create mappings in both directions
            else:
                s_to_t[c1] = c2
                t_to_s[c2] = c1

        return True


class Solutiontest:
    def test_isIsomorphic(self) -> None:
        soln: Solution = Solution()
        assert soln.isIsomorphic(s="egg", t="add") == True
        assert soln.isIsomorphic(s="vai", t="vai") == True


if __name__ == '__main__':
    soln_test: Solutiontest = Solutiontest()
    soln_test.test_isIsomorphic()