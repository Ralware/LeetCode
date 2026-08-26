def maxProfit(Prices):
    Max = 0
    for Index in range(len(Prices)):
        MaxValue = max(Prices[Index:])
        Profit = MaxValue - Prices[Index]
        if Profit > Max:
            Max = Profit
    return Max


print(maxProfit([7,1,5,3,6,4]))
