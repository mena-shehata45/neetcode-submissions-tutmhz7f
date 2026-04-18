class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        heap = []
        for num in nums:
            if num not in occ:
                occ[num] = 1
            else:
                occ[num] += 1

        for num, freq in occ.items():
            heapq.heappush(heap, (freq, num)) 

            if len(heap) > k:
                heapq.heappop(heap)
                
        return [pair[1] for pair in heap]

