class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        total_xor = 0
        for x in nums:
            total_xor ^= x
        
        if total_xor != 0:
            return n
        
        if any(x != 0 for x in nums):
            return n - 1
        
        return 0
        