class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        
        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
            
        freq = list(seen.items())
        freq.sort(key = lambda x: x[1])
        freq.reverse()
        
        res = []
        
        while k:
            res.append(freq[0][0])
            freq.pop(0)
            k -= 1
            
        return res
        