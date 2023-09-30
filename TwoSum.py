class Solution:
  def twoSum(self,nums,target):
      indices={}
      
      for i,n in enumerate(nums):
          diff=target-n
          if diff in indices:
              return [indices[diff],i]
          indices[n]=i
        
"""sol=Solution()
b=[4,8,7,6,5]
t=15
sum=sol.twoSum(b,t)
print(sum)"""