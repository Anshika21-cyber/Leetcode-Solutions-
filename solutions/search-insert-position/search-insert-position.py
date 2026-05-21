class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        b=len(nums)-1
            
        while l<=b:
            mid=(l+b)//2
            if nums[mid]==target:
                return mid

            elif target< nums[mid]:
                b=mid-1

            else:
                l=mid+1

        return l
    
                