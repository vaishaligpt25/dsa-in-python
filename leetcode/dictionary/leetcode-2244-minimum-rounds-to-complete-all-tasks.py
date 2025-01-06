# LeetCode-2244: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

# barely passing: bottom 5% in speed

from typing import Dict, List


class Solution:
    INFINITE: int = 2000000000

    def _create_task_freq_dict(self, tasks: List[int]) -> Dict[int, int]:
        freq_dict: Dict[int, int] = {}
        for task in tasks:
            curr_freq: int = freq_dict.get(task, 0)
            freq_dict[task]: int = curr_freq + 1
        return freq_dict

    def _find_min_steps(self, freq: int) -> int:
        min_steps: int = Solution.INFINITE
        for no_of_2_task_steps in range(0, freq + 1):
            no_of_3_task_steps: int = int((freq - (2 * no_of_2_task_steps)) / 3)

            is_valid_solution: bool = ((2 * no_of_2_task_steps) + (3 * no_of_3_task_steps)) == freq
            if is_valid_solution:
                curr_steps: int = no_of_2_task_steps + no_of_3_task_steps
                min_steps: int = min(min_steps, curr_steps)
        return min_steps

    def minimumRounds(self, tasks: List[int]) -> int:
        freq_dict: Dict[int, int] = self._create_task_freq_dict(tasks=tasks)

        total_no_of_steps: int = 0
        for _, freq in freq_dict.items():
            steps: int = self._find_min_steps(freq=freq)
            if steps == Solution.INFINITE:
                return -1
            total_no_of_steps: int = total_no_of_steps + steps

        return total_no_of_steps
