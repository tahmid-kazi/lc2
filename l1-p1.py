class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1244-1249pm) new repo setup
        # 1249-1254pm) .gitignore
        # 1254-1259pm)(3/30/25)(Sun) L1 - done
        
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []
