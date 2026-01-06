class Solution:
    def reverse(self, x: int) -> int:
       if x<0:
            y=abs(x)
            num=str(y)
            rev=num[::-1]
            reversed_number=-int(rev)

       else:
            num=str(x)
            rev=num[::-1]
            reversed_number=int(rev)


       if reversed_number< -2**31 or reversed_number> 2**31 -1:
            return 0

       else:
           return reversed_number