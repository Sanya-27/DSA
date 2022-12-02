class Solution:
   def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        m=0
        l=0
        h=n-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==2:
                nums[h],nums[m]=nums[m],nums[h]
                h-=1
            else:
                m+=1
                