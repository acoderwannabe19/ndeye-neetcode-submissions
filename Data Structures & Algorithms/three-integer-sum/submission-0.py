class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet_list = []
        for i in range(len(nums) - 2):
            # Skip duplicate values of i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1

            while j < k:
                if nums[i] == -(nums[j] + nums[k]):
                    triplet_list.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                        
                elif (nums[j] + nums[k]) < - nums[i]:
                    j+=1
                else:
                    k-=1


        return triplet_list