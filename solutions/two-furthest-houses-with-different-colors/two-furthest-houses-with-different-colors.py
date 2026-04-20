class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=0
        dist=0
        for i in range(len(colors)):
            for j in range (i+1,len(colors)):

                if colors[i]!=colors[j]:
                    value=abs(i-j)
                    
                    if value>=dist:
                        dist=value
        return dist

        