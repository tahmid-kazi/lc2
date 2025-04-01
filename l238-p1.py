class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # L238 done: (3/31/25)(Mon)(945/1015-1017pm)
        res = [1] * len(nums)
        prefix  = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
