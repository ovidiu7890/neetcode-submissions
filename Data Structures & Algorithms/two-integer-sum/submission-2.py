class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        n = len(nums)
        l = {}
        res = []
        for i in range(n):
            l[nums[i]]=i
        for i in range(n):
            if(target-nums[i] in l):
                if(l[target-nums[i]] != i):
                    res.append(i)
                    res.append(l[target-nums[i]])
                    return res
        return res

                