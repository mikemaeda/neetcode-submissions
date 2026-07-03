class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] += 1 
            else:
                countS[s[i]] = 1

        for i in range(len(t)):
            if t[i] in countT:
                countT[t[i]] += 1
            else:
                countT[t[i]] = 1 
            
        return countS == countT


            
    

        
        
        




#loop through the entire string, check 
#whether the string matches the input, 
#it doesnt matter order at all 

        