class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_map = {}
        for num in nums:
           freq_map[num] = freq_map.get(num, 0) + 1


        heap = []
        for num in freq_map.keys():
            heapq.heappush(heap, (freq_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

