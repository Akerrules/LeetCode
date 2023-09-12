class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        #create a list to add letters
        # merge the letter in the list 
        # convert it to string

        l = []

        for i in range((max(len(word1),len(word2)))):
            if(i<len(word1)):
                l.append(word1[i])
            if(i<len(word2)):
                l.append(word2[i])
        
        return ("".join(l))