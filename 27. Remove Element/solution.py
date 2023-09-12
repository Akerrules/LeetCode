class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        tmplist = []

        total = 0
        for i in nums: ## get filtered out elements
            if(i!=val):
               tmplist.append(i) 
               total = total+1

        for i in range(len(nums)): # transfer the filtered elements to the orginal array
            if(i<len(tmplist)):
                nums[i] = tmplist[i]
            else:
                nums[i]=-1
        return total