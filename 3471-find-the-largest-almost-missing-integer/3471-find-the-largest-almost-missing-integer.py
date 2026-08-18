from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        candidates = sorted(set(nums), reverse=True)
        
        for x in candidates:
            count = 0
            for start in range(n - k + 1):
                if x in nums[start:start + k]:
                    count += 1
                    if count > 1:
                        break
            if count <= 1:
                return x
        return -1
        