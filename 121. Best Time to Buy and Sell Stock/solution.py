class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #goal find the maximum difference

        max_ = 0
        min_ = 0
        result =0
        for i in range(len(prices)):
            if(prices[i]< prices[min_]):
                min_ = i
                max_ = i
            elif(prices[i]> prices[max_] and min_< i):
                max_ = i
                result = max(result,prices[max_]-prices[min_])
            # print(result,prices[max_],prices[min_])

        return result