class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values={}

        for i, num in enumerate(nums):
            values[num]=i
        
        for i, num in enumerate(nums):
            compl=target - num

            if compl in values and values[compl]!=i:
                return [i , values[compl]]
                