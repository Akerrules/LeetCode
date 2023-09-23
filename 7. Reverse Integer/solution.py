class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        result  = ""
        neg = False
        for i in range(len(s)):
            if(s[i] == '-'):
                neg = True
            else:
                result  = s[i]+result
        if(neg):
            result = "-" + result
        result  = int(result)
        if(result < (-2**(31)) or result> ((2**31)-1)): 
            return 0 
        return result