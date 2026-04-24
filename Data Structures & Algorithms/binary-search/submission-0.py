class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        dr = len(nums) - 1
        while st<=dr:
            mij = (st + dr) // 2
            if nums[mij] == target:
                return mij
            elif nums[mij] < target:
                st = mij + 1
            else:
                dr = mij - 1
        return -1

        