class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        c=Counter(nums)
        res_p=c.most_common(k)
        for i in res_p:
            res.append(i[0])
            
        return res