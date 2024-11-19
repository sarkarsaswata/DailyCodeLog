from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_combination, current_sum):
            if len(current_combination) == k and current_sum == n:
                result.append(list(current_combination))
                return
            if len(current_combination) > k and current_sum > n:
                return
            
            for num in range(start, 10):
                current_combination.append(num)
                backtrack(num+1, current_combination, current_sum+num)
                current_combination.pop()
        
        backtrack(1, [], 0)
        return result
            