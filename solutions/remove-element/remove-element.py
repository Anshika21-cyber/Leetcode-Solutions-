class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k=0
        # for i in range (len(nums)):
        #     if (nums[i]==val):
        #         # nums.remove(val)
        # else:
        #     k+=1
        # return k
        # I can't use above method because its will chnge the existing list while its current loop is running 
        
        k=0 
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k

        