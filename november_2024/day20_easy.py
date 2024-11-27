from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        if not s:
            for d in digits:
                s += str(d)
        s = int(s) + 1
        return list(map(int, str(s)))