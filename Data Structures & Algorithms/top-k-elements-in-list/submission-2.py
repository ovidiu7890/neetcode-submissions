class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = defaultdict(int)
        res = []
        for i in nums:
            has[i] +=1
        while k>0:
            maxi = 0
            hr = 0
            for key in has:
                if has[key]>maxi:
                    maxi = has[key]
                    hr = key
            res.append(hr)
            has[hr] = 0
            k-=1
        return res
                
        

        