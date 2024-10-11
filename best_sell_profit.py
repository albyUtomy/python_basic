class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        lowest_price = prices[0]
        max_profit = 0
        

        for price in prices:
            lowest_price = min(lowest_price, price)
            max_profit = max(max_profit, price - lowest_price)

        return max_profit


        # if not prices:
        #     return False
        
        # lowest_p = prices.index(min(prices))
        # sliced_l = prices[lowest_p:]
        # if not sliced_l:
        #     return False
        # else:
        #     highest_s = max(sliced_l)
        #     return (prices.index(highest_s)+1)