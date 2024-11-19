from typing import List
# O(n) solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_length = float('inf')
        current_sum = 0

        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return 0 if min_length == float('inf') else min_length