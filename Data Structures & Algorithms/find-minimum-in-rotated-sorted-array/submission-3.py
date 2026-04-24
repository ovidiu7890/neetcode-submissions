class Solution:
    def findMin(self, nums: list[int]) -> int:
        st = 0
        dr = len(nums) - 1
        
        while st < dr:
            mij = (st + dr) // 2
            
            if nums[mij] > nums[dr]:
                st = mij + 1
            else:
                dr = mij
                
        return nums[st]