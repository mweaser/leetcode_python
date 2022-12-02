class Solution:
    def groupAnagrams(self, ele: List[str]) -> List[List[str]]:
        
        words = []
        for e in ele:
            words.append(list(e))
                    
        seen = {}
        res = []
        
        for w in words:
            sorted_w = "".join(sorted(w))
            if sorted_w not in seen:
                seen[sorted_w] = []
            seen[sorted_w].append("".join(w))
        
        return seen.values()
        