class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list=[]
        seen = set()
        for i  in range(len(strs)):
            if strs[i] in seen:
                continue
            sublist=[]
            target_counter = Counter(strs[i])
            for str_val in strs: 
                if target_counter == Counter(str_val):
                    sublist.append(str_val)
                    seen.add(str_val)

            if sorted(sublist) not in final_list:
                final_list.append(sorted(sublist))
                sublist=[]
        return final_list