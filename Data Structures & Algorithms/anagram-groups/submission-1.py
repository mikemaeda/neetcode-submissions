class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs: 
            key = "".join(sorted(word))
            if key not in groups: 
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())

#create an emppty dictionary 
#loop throuhg word in the list 
#sort every word - make it the key of the dict
#if statement - add all values to the original  key (append)
# #output the values not keys (.values)
# Intuition

# My first thought was that anagrams 
# become identical if their letters are sorted.

# So, I can sort every word and use the
#  sorted version as a key in a dictionary.

# Words with the same sorted key belong in the same group.

# Approach

# 1. Create an empty dictionary called groups.
# 2. Loop through every word in strs.
# 3. Sort the word and convert it back into 
# a string to create a key.
# 4. If the key does not exist in groups, create 
# an empty list for it.
# 5. Add the original word to the list for that key.
# 6. Return all the lists stored in the dictionary.

# Complexity

# * Time Complexity: O(m * n log n)
# * Space Complexity: O(m * n)

# groups.keys()     # Gives all the keys
# groups.values()   # Gives all the values
# groups.items()    # Gives both key and value pairs
