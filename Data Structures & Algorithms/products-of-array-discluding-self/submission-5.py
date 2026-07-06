class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultat=[]
        res=1
        zero_count=0
        index_zero=0        
        for i in range(len(nums)):
            if nums[i]!=0:
                res=res*nums[i]
                
            if nums[i]==0:
                index_zero=i
                zero_count+=1
        if zero_count>1:
            return [0]*len(nums)
        if zero_count==1:
            for j in range(len(nums)):
                if j==index_zero:
                    resultat.append(res)
                else: 
                    resultat.append(0)
            return resultat
        for j in range(len(nums)):
            resultat.append(res//nums[j])
        return resultat