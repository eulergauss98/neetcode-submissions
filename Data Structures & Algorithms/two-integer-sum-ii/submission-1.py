class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_list=list(dict.fromkeys(numbers))
        start=0
        end=len(new_list)-1
        while start<end:
            if new_list[start]+new_list[end]==target:
                return [start+1,end+1]
            if new_list[start]+new_list[end]<target: 
                start+=1
            if new_list[start]+new_list[end]>target:
                end-=1
            