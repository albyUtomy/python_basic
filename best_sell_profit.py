def maxProfit(prices) -> int:
    if not prices:
        return 0

    lowest_price = prices[0]
    max_profit = 0
        

    for price in prices:
        lowest_price = min(lowest_price, price)
        max_profit = max(max_profit, price - lowest_price)

    return max_profit



List_p = [2,3,7,1,6,7,8,9]
print(maxProfit(List_p))
