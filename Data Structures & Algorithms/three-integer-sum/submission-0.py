class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k= len(nums)-1
            while j<k:
                if -nums[i] == nums[j] + nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                    inter1 = nums[j]
                    inter2 = nums[k]
                    j+=1
                    k-=1
                    while j<k and inter1 == nums[j]:
                        j+=1
                    while j<k and inter2 == nums[k]:
                        k-=1
                elif -nums[i] < nums[j] + nums[k]:
                    k-=1
                else:
                    j+=1
        return res

