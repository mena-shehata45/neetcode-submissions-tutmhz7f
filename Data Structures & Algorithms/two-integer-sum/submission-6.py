class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hash_ = dict()
            for n in range(len(nums)):
                pair = target - nums[n]
                if pair in hash_:
                    return sorted([n, hash_[pair]])
                else:
                    hash_[nums[n]] = n 
