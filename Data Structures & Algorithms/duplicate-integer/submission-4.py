class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        read = set()

        for num in nums: 
            if num in read:
                return True 
            else: 
                read.add(num)
        return False



        