class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances =[(math.sqrt(x1*x1 + y1*y1), [x1, y1]) for x1, y1 in points]
        # print(distances)
        heapq.heapify(distances)
        res = []
        for i in range(k):
            distance, point = heapq.heappop(distances)
            res.append(point)
        
        return res