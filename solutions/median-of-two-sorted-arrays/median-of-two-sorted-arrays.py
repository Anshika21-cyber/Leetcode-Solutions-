class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=[]
        i=j=0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1

        while i<len(nums1) :
            nums3.append(nums1[i])
            i+=1

        while j<len(nums2) :
            nums3.append(nums2[j])
            j+=1

        l=len(nums3)
        if l%2==0:
            # (//)give int division
            return (nums3[(l//2)]+nums3[(l//2-1)])/2


        if l%2!=0:
            return nums3[l//2]


            

                      




                    
