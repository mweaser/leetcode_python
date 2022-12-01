class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        
        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
            
        res = list(seen.items())  
        res.sort(key = lambda x: x[1])
        res.reverse()
        
        final = []
        
        while k:
            final.append(res[0][0])
            res.pop(0)
            print("res is now: ", res)
            k-=1
        
        return final
        