class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        dr = len(nums) - 1

        
        if st == dr:
            if nums[st] == target:
                return 0
            else:
                return -1


        if nums[st] > nums[dr]:
            while st<dr:
                mij = (st+dr)//2
                if nums[mij]> nums[dr]:
                    st = mij+1
                else:
                    dr = mij
            
            
            if nums[st]<=target and target <= nums[len(nums)-1]:
                dr = len(nums)-1
            else:
                dr = st -1
                st = 0
                

        print(st, dr)
        
        while st<=dr:
            mij = (st+dr)//2
            if nums[mij] == target:
                return mij
            elif nums[mij] >= target:
                dr = mij - 1
            else:
                st = mij + 1

        return -1


            

