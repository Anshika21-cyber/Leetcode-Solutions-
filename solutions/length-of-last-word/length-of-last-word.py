class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s[::-1].split()

        p=len(l[0])

        return p

        # a=s.split()
        # for i in range(len(a)):
        #     if i==len(a)-1:
        #         p=len(a[i])

        # return p
       
        