class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        if(low==high):
            return low
        while(low<=high):
            mid=(low+high)//2
            if(mid==0):
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low=mid+1
            elif (mid==len(nums)-1):
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    high=mid-1
            elif(mid>0 and mid <n-1 and nums[mid+1]<nums[mid] and nums[mid-1]<nums[mid]):
                return mid
            elif(mid>0 and nums[mid]<nums[mid-1]):
                high=mid-1
            elif(mid<n-1 and nums[mid]<nums[mid+1]):
                low=mid+1