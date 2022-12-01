class Solution:
    def groupAnagrams(self, ele: List[str]) -> List[List[str]]:
        
        words = []
        seen = {}
        res = []
        
        for e in ele:
            words.append(list(e))
            
        for w in words:
            curr = ''.join(sorted(w))
            
            if curr not in seen:
                seen[curr] = []
            seen[curr].append(''.join(w))
            
        return seen.values()