class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1
        
        # Sort items by frequency (highest first)
        sorted_items = sorted(freq_count.items(), key=lambda x: x[1], reverse=True)
        
        # Extract only the top k numbers
        results = [num for num, freq in sorted_items[:k]]
        
        return results