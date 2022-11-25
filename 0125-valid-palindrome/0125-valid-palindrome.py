class Solution:
    def isPalindrome(self, s: str) -> bool:
        
      
        s = s.lower()
        s_list = []
        
        for i in range(len(s)):
            ascii_val = ord(s[i])
            if (ascii_val >= 97 and ascii_val <= 122) or (ascii_val >= 48 and ascii_val <= 57):
                s_list.append(s[i])
         
        print(s_list)
        
               
        if len(s_list) <= 1:
            return True

        l = 0
        r = len(s_list) - 1
        while l < r:
            print("s[l]:", s[l])
            print("s[r]:", s[r])
            
            if s_list[l] != s_list[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
            
            
            
        
        