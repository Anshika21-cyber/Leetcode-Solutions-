# class Solution:
#     def longestPalindrome(self, s: str) -> str: 
#         i=0
#         j=1
#         p=[]
#         m=0
#         final=""
#         for i in range (len(s)-1):
#             remain= s[i:]
#             p.append(s[i])
#             if s[i]==s[j] and j<len(s):
#                while j<len(s) and s[i]==s[j]:
#                    p.append(s[j])
#                    j+=1
#             elif remain.count(s[i])>=3:
#                 while s[i]!=s[remain.rfind(s[i])] and j<len(s):
#                    p.append(s[j])
#                    j+=1
#                    l=len(p)
#                    if p==p[::-1]:
#                         m=max(l,m)
#                         if m>l:
#                             pass
#                         else:
#                            final="".join(p)
#                 #         return p

#                 # if p==p[::-1]:
#                 #     pass
#                 if j<len(s) and s[i]==s[j]:
#                     p.append(s[j])
#             elif s[i]!=s[j] and j<len(s):
#                while j<len(s) and s[i]!=s[j]:
#                    p.append(s[j])
#                    j+=1
                
#                if j<len(s) and s[i]==s[j]:
#                     p.append(s[j])
            
#             l=len(p)
#             # Check palindromic string
#             if p==p[::-1]:
#                 m=max(l,m)
#                 # Check longest string
#                 if m>l:
#                    p.clear()
#                    j=i+2
#                 else:
#                     final="".join(p)
#                     p.clear()
#                     j=i+2
#             else:
#                 p.clear()
#                 j=i+2
#          # return final

#         if len(final)>0:
#             return final
#         else:
#             return s[0]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            p1 = expand(i, i)     # odd length
            p2 = expand(i, i+1)   # even length

            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2

        return res






        