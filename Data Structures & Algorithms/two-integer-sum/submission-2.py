class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in memory:
                return [memory[complement], i]

            memory[num] = i





























        
             
            


# Intuition

# My first thought was that for every number, 
#I can calculate the number I need to reach the target.

# If I’ve already seen that number before, then 
#I’ve found my pair and can return their indices immediately.

# Otherwise, I store the current number and its 
# index so future numbers can use it as their match.

# Approach

# 1. Create an empty dictionary called prevMap.
# 2. Loop through nums using both the index i and value n. use enumerate in python 
# 3. Calculate diff = target - n.
# 4. Check if diff already exists in prevMap.
# 5. If it does, return the stored index and the current index.
# 6. Otherwise, store the current number and its index in prevMap.
# 7. Continue until the pair is found.

# Complexity

# * Time Complexity: O(n)
# * Space Complexity: O(n)

               

            
            






