class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        org=x
        pal=0

        while x!=0:
            pal=pal*10+x%10
            x=x//10
            
        return org==pal
          
sol=Solution()
x=int(input("Enter a number :"))
result=sol.isPalindrome(x)
print(result)