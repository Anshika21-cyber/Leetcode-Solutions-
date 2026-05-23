class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in range (len(digits)):
            s+=str(digits[i])

        num= int(s) +1
        ans=[]

        for i in str(num):
            ans.append(int(i))

        return ans 


