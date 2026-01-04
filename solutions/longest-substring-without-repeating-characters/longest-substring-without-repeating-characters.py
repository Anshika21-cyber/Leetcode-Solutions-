class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            substring=[]
            for j in range(i,len(s)):
                if s[j] in substring:
                    break
                substring.append(s[j])
            l=len(substring)
            m=max(m,l)
        return m
