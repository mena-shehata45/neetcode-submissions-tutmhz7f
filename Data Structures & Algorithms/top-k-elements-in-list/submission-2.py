class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for num in nums:
            if num not in occ:
                occ[num] = 1
            else:
                occ[num] += 1

        list_of_freq = [(freq, num) for num, freq in occ.items()] 
        heapq.heapify(list_of_freq)
        
        while len(list_of_freq) > k:
            heapq.heappop(list_of_freq)

        return [pair[1] for pair in list_of_freq]

