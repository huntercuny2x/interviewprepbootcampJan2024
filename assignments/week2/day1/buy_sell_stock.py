def maxProfit(prices):
    l=max_gains=0
    for r in range(len(prices)):
        if prices[r] < prices[l]:
            l=r

        max_gains=max(max_gains,prices[r]-prices[l])
    return max_gains 