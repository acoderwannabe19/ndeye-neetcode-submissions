class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right  # start with max as a safe upper bound

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(p / mid) for p in piles)

            if total_hours <= h:
                res = mid  # mid is possible, but try smaller
                right = mid - 1
            else:
                left = mid + 1  # need to eat faster

        return res