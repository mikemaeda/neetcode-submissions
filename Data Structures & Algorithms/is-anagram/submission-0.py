class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
    
        return sorted(s) == sorted (t)




#loop through the entire string, check 
#whether the string matches the input, 
#it doesnt matter order at all 

        