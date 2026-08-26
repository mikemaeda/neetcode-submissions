class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # If the list is empty, return an empty string
        if not strs:
            return ""

        # Use the first word as our reference
        first_word = strs[0]

        # Go through each character position in the first word
        for i in range(len(first_word)):

            # Check that same position in every other word
            for word in strs[1:]:

                # If the word is too short OR the characters don't match
                if i >= len(word) or word[i] != first_word[i]:
                    return first_word[:i]

        # If no mismatch was found
        return first_word