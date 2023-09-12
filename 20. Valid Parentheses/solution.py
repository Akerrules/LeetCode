class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"{":"}", "(":")","[":"]"}
        stack =[]
        prev = ""

        for i in range(len(s)):
            if(stack!=[]):
                if((stack[-1] not in dic)):
                    break
                if(s[i]==dic[stack[-1]]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return not bool(stack)