class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h={}
        l=[]
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
        a=list(h.values())   
        b=list(h.keys())
        for i in range(len(a)):
            if a[i]==1:
                p=a.index(a[i])
                m=b[i]
                l.append(m)     
        return m