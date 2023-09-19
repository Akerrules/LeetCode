class Solution:
    def longestValidParentheses(self, s: str) -> int:
       
       #if stack is clear then take max
        tmp=0
        high= 0
        i=0
        stack= []
        stack.append(-1)
        while i<len(s):

            if(s[i]=="("):
                stack.append(i)
            else:
                if(len(stack)!=0):
                    stack.pop()

                if(len(stack)!=0):
                    high = max(high,i - stack[len(stack)-1])
                else:
                    stack.append(i)
           
            i=i+1
            
        return high