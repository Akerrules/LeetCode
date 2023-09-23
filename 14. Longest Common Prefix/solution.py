class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i=0
        word = strs[0]
        result = ""
       
        if(len(strs)<=0):
            return ""
        elif (len(strs)==1):
            return strs[0]
        while i<len(strs):
            for j in range(len(word)):   
                if(j>len(strs[i])-1 or word[j]!=strs[i][j]):
                    if(j==0):
                        return ""
                    print(word[0:j])
                    word  = word[0:j]
                    result=word
                    break
            i = i+1
        return word