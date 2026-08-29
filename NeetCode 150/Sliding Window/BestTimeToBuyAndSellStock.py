# Input: Prices = [10,1,5,6,7,1]
# Output: 6


def maxProfit(Prices):
    
    Min = Prices[0]
    MaxDiff = 0
    for Index in range(len(Prices)):
        if Prices[Index] < Min:
            Min = Prices[Index]
        
        Diff = Prices[Index] - Min
        
        if Diff > MaxDiff:
            MaxDiff = Diff
    
    return MaxDiff

