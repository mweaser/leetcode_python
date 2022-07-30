class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        start = 0
        end = len(letters) - 1
        
        while start <= end:
            middle = start + (end - start) // 2
            
            if target < letters[middle]:
                end = middle - 1
            else:
                start = middle + 1
        
        return letters[start % len(letters)]