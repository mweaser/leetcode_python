class Solution:
    def groupAnagrams(self, ele: List[str]) -> List[List[str]]:
        
        seen = {}
        
        for e in ele:
            s = "".join(sorted(list(e)))
            
            if s not in seen:
                seen[s] = []
            seen[s].append(e)
        
        return seen.values()
        