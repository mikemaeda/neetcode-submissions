class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1 
            else:
                count[num] = 1
    #dictionary.get(key, default_value) i can say this 
        
        arr = [] 
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort() 

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res








# Intuition

# My first thought was to count how often each number appears.

# After I have the frequencies, I can sort the numbers by their frequency and take the top k.

# Approach

# 1. Create a dictionary called count.
# 2. Count how many times each number appears in nums.
# 3. Create an array called arr.
# 4. Store each number as [frequency, number] so Python sorts by frequency.
# 5. Sort arr.
# 6. Pop from the end of arr because the highest frequencies are at the end.
# 7. Add those numbers to res until res has k elements.
# 8. Return res.

# Complexity

# * Time Complexity: O(n log n)
# * Space Complexity: O(n)       