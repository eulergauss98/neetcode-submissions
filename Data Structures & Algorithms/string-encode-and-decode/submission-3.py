class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "vide" 
        return "€".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="vide":
            return []
        return s.split("€")
