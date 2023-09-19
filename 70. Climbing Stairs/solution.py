class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=3):
            return n
            
        l = []
        for i in range(n):
           l.append(1)
        
        l[0] = 1
        l[1] = 2
        l[2] = 3

        for i in range(3,n):
            l[i] = l[i-1]+l[i-2]
            print(l)
            
        return l[-1]

        