# leetcode_59_https://leetcode.com/problems/buddy-strings


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If lengths are different, they can't be buddy strings
        if len(s) != len(goal):
            return False

        # If strings are identical, we need to check if we can swap any two same characters
        if s == goal:
            # If there are any duplicate characters, we can swap them
            return len(set(s)) < len(s)

        # Find positions where characters differ
        differences = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append(i)

        # We should have exactly 2 differences for valid buddy strings
        if len(differences) != 2:
            return False

        # Check if swapping these positions makes the strings equal
        i, j = differences
        return s[i] == goal[j] and s[j] == goal[i]
