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
#output the values not keys (.values)


