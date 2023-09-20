class Solution:
    def longestPalindrome(self, s: str) -> int:
        #if even put on both sides
        #if odd then can only have one odd

        dic = {}
        counter =0
        odd  = False

        for i in s:
            if(i in dic):
                dic[i]= dic[i]+1
            else:
                dic[i]=1

        for i in dic:
            if(dic[i]%2!=0):
                if(odd==False):
                    odd =True
                    counter = counter+dic[i]
                else:
                    counter = counter + dic[i]-1
            else:
                
                counter = counter+dic[i]
        return counter


        