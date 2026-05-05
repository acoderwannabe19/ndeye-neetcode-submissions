class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            
            # Add current subset
            result.append(path[:])
            print(path)
            
            for i in range(start, len(nums)):
                # Choose
                path.append(nums[i])
                
                # Explore
                backtrack(i + 1, path)
                
                # Undo (backtrack)
                path.pop()
        
        backtrack(0, [])
        return result