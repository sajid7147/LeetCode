class Solution(object):
    def romanToInt(self, s):

        roman_numerals={
           'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000
        }
        
        prevValue=0
        result=0

        for numeral in reversed(s):
             value=roman_numerals[numeral]
             
             if value<prevValue:
                 result-=value
             else:
                 result+=value
             
             prevValue=value
        return result