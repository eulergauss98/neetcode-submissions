class Solution:
    def isPalindrome(self, s: str) -> bool:
        int_s=re.sub(r'[^0-9a-zA-Z]', '', s)
        new_s=int_s.lower()
        for i in range(len(new_s)) :
            j=len(new_s)-i-1
            if new_s[i]==new_s[j]:
                continue
            else : 
                return False
        return True

