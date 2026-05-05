class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        non_val = 0
        l = len(nums)

        for i in range(l):
            if nums[i] != val:
                nums[non_val] = nums[i]
                non_val += 1
        
        return non_val


        