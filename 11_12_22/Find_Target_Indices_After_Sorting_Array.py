class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller=0
        larger=0
        l=[]
        for i in range(len(nums)):
            if nums[i]<target:
                smaller+=1
            elif nums[i]>target:
                larger+=1
        for i in range(smaller,len(nums)-larger):
            l.append(i)
        return l