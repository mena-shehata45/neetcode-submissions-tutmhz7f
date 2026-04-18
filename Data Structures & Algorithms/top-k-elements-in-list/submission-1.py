class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for num in nums:
            if num not in occ:
                occ[num] = 1
            else:
                occ[num] += 1

        sorted_list = sorted(occ.items(), key=lambda x: x[1], reverse=True)
        sorted_list = [pair[0] for pair in sorted_list[:k]]
        print(sorted_list)
        return sorted_list
