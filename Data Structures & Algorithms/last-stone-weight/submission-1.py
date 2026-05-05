class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)
            
        stones.append(0) # make sure the final heap has something

        return abs(stones[0])
