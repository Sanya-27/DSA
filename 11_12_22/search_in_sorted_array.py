class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while ( start <= end ):
            mid = ( start + end ) // 2
            
            if nums[mid] == target:
                return mid
            elif( start == mid == end ):
                return -1        
            elif ( nums[start] <= nums[mid] ):
                if( nums[start] <= target < nums[mid] ):
                    end = mid
                else:
                    start = mid + 1
            else:
                if ( nums[mid] < target < nums[start] ):
                    start = mid + 1
                else:
                    end = mid

    
