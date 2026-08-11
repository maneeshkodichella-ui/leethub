class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # find length of sequential prefix
        i = 1
        while i < n and nums[i] == nums[i-1] + 1:
            i += 1
        s = sum(nums[:i])
        
        num_set = set(nums)
        while s in num_set:
            s += 1
        return s
        