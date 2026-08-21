class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CS = {}
        CT = {}

        for char in s:
            if char in CS:
                CS[char]  += 1
            else:
                CS[char] = 1
        for char in t:
            if char in CT:
               CT [char] += 1 
            else:
                CT [char] = 1
        
        if CT == CS:
            return True
        
        return False


                
    

# Intuition

# My first thought was that anagrams must contain the exact same characters the exact same number of times.

# So, I can count how many times each character appears in s and how many times each character appears in t.

# If the two counts are identical, then the strings are anagrams.

# Approach

# 1. Create two dictionaries: countS and countT.
# 2. Loop through s and count how many times each character appears.
# 3. Loop through t and count how many times each character appears.
# 4. Compare the two dictionaries.
# 5. If they are equal, return True; otherwise, return False.

# Complexity

# * Time Complexity: O(n + m)
# * Space Complexity: O(n + m)

            
    

        
        
        


 

        