class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionnary = {}
        for i, num in enumerate(nums):
            diff =  target - num
            if diff in dictionnary:
                return [dictionnary[diff], i]
            dictionnary[num] = i


        