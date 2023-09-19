class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        high  = n
        low =0

        while(low<=high):
            mid = (high+low)//2
            if(isBadVersion(mid)):
                high  = mid-1
            if(not isBadVersion(mid)):
                low = mid+1
            
        
        return low