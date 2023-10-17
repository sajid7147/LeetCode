class Solution(object):
    def plusOne(self, digits):
        carry=1

        for i in range(len(digits)-1,-1,-1):
            sum=digits[i]+carry
            digits[i]=sum%10
            carry=sum//10
        
        if carry:
            digits.insert(0,1)
        
        return digits
        