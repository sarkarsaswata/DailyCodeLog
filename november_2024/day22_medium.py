from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_combination, current_sum):
            # Base case: if current_sum equals target, add the combination to the result
            if current_sum == target:
                result.append(list(current_combination))
                return
            # If current_sum exceeds target, stop exploring this path
            if current_sum > target:
                return

            # Iterate through the candidates starting from the current index
            for i in range(start, len(candidates)):
                # Include the current candidate and move forward
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                # Backtrack: remove the last added element
                current_combination.pop()

        # Start the backtracking process
        backtrack(0, [], 0)
        return result