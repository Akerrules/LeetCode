class Solution:
    def search(self, nums: List[int], target: int) -> int:

        min = 0
        max = len(nums)-1
        while(min<=max):
            mid = min + (max -  min)//2
            if(nums[(max+min)//2]==target):
               return (max+min)//2
            elif(nums[(max+min)//2] < target):
                min = mid+1
            else:
                max = mid-1
        return -1