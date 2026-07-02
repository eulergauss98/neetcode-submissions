class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sort_list=defaultdict(list)
        
        
        for str in strs: 

                sort_list[''.join(sorted(str))].append(str)

        return list(sort_list.values())

        