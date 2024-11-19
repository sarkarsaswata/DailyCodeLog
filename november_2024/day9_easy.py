from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or len(nums) == len(set(nums)):
            return False
        
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and abs(i - last_seen[num]) <= k:
                return True
            last_seen[num] = i
        return False