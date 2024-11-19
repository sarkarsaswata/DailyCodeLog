from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for amount in houses:
                new_prev1 = max(prev1, prev2+amount)
                prev2 = prev1
                prev1 = new_prev1
            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        case1 = rob_linear(nums[1:])
        case2 = rob_linear(nums[:-1])

        return max(case1, case2)