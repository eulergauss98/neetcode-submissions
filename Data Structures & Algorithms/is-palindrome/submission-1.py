class Solution:
    def isPalindrome(self, s: str) -> bool:
        int_s=re.sub(r'[^0-9a-zA-Z]', '', s)
        new_s=int_s.lower()
        chaine_inverse = ''.join(reversed(new_s))
        if chaine_inverse==new_s:
            return True 

        else : 
            return False 


