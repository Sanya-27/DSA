class Solution:
   def sortColors(self, nums: List[int]) -> None:
        l=len(nums)
        mid=0
        low=0
        high=l-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==2:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
            else:
                mid+=1
                #sort colors