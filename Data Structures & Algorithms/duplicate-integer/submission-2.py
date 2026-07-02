class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        if len(nums) not in range(0, 10**5 + 1): 
            return False

        for i in range(len(nums)):
            if nums[i] not in range(-10**9, 10**9 + 1):
                return False
            
            if nums[i] in seen:
                return True
            
            else:
                seen.add(nums[i])
            
        return False
            
                
    