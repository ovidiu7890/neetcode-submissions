class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        maxi =0
        for i in my_set:
            if i-1 in my_set:
                continue
            else:
                j = i
                number = 0
                while j in my_set:
                    number+=1
                    j+=1
                if number > maxi:
                    maxi = number
        return maxi
        