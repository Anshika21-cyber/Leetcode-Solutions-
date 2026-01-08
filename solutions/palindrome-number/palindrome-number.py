class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=abs(x)
        s=str(y)
        rev=s[::-1]
        o=int(rev)
        if o==x:
            return True
        else:
             return False
        