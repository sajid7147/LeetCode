class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        i=0
        n=0

        while i<len(nums):
            if nums[i]!=val:
                nums[n]=nums[i]
                n+=1
            i+=1
        
        return n
        