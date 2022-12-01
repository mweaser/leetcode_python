class Solution:
    def groupAnagrams(self, ele: List[str]) -> List[List[str]]:
        
        if not ele:
            return
        
        
        res = []
        for i in range(len(ele)):
            res.append(list(ele[i]))
        
        seen = {}
        
        for i in range(len(res)):
            curr = str(sorted(res[i]))    
            if curr not in seen:
                seen[curr] = []
            
            seen[curr].append(''.join(res[i]))
                
        final = []    
        for s in seen:
            final.append(seen[s])
            
        return final
        
            