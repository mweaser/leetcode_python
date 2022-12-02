class Solution:
    def groupAnagrams(self, ele: List[str]) -> List[List[str]]:
                    
        seen = {}
        res = []
        
        for w in ele:
            sorted_w = "".join(sorted(list(w)))
            if sorted_w not in seen:
                seen[sorted_w] = []
            seen[sorted_w].append("".join(w))
        
        return seen.values()
        