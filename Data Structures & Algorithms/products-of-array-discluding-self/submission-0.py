class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1] * l
        suffix = [1] * l
        result = [1] * l

        # Build prefix products
        for i in range(1, l):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix products
        for i in range(l - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Combine them
        for i in range(l):
            result[i] = prefix[i] * suffix[i]

        return result


        