class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = list(s)
        
        tmp = ""
        for i in range(len(l)-1,-1,-1):
            tmp = tmp+l[i]
        return s == tmp