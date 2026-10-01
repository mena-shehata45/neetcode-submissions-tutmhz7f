class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict_ :
                return sorted([i, dict_[difference]])
            dict_[nums[i]] = i
