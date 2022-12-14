class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr)==2:
            return True
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != arr[i-1]-arr[i-2]:
                return False
        return True