class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        last=-1
        first=-1
        for i in range (len(nums)):
            if nums[i]==target:
                if first==-1:
                    first=i
                last=i
        return first,last
                
