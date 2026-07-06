class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultat=[]
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if i!=j:
                    res=res*nums[j]
            resultat.append(res)
        return resultat