# leetcode_2351:https://leetcode.com/problems/first-letter-to-appear-twice


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s_map: dict[str, int] = {}
        for char in s:
            if char in s_map:
                return char
            s_map[char] = 1
        return ""

    def repeatedCharacter1(self, s: str) -> str:
        seen: set[str] = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return ""


class SolutionTest:
    def check_repeatedCharacter(self) -> None:
        soln: Solution = Solution()
        assert soln.repeatedCharacter(s="abccbaacz") == "c"
        assert soln.repeatedCharacter(s="abcdd") == "d"
