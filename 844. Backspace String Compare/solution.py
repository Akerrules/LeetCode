class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        a = []
        b = []

        for i in range(len(s)):
            if(s[i]=="#" and len(a)!=0):
                a.pop()
            elif(s[i]!="#"):
                a.append(s[i])
        
        for i in range(len(t)):
            if(t[i]=="#" and len(b )!=0):
                b.pop()
            elif(t[i]!="#"):
                b.append(t[i])
        
        if(len(a)==len(b)):
            for i in range(len(a)):
                if(a[i]!=b[i]):
                    return False
        else:
            return False
        return True