class Solution(object):
    def addBinary(self, a, b):
      result=[]
      carry=0

      len_a,len_b=len(a),len(b)
      max_len=max(len_a,len_b)
      a=a.zfill(max_len)
      b=b.zfill(max_len)

      for i in range(max_len-1,-1,-1):
          bit_a=int(a[i])
          bit_b=int(b[i])

          sum = bit_a + bit_b + carry
          result.append(str(sum%2))
          carry=sum//2

      if carry:
          result.append(str(carry))
      
      result=result[::-1]
      return ''.join(result)



