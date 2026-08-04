class Solution:
    def findMissingElements(self, nums):
        nums_set = set(nums)
        ans = []

        for i in range(min(nums), max(nums) + 1):
            if i not in nums_set:
                ans.append(i)

        return ans
        