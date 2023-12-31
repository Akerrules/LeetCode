class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        mid = (high + low)//2
        result = 0
        while low <= high:
            mid  = (high + low)//2
            if(nums[mid] > target):
             high = mid-1
            elif(nums[mid]<target):
                low  = mid+1
            else: 
                return mid
                
        return low