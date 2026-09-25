def findLengthOfLCIS(Nums):

    Count = 1
    MaxCount = 1

    for Index in range(1, len(Nums)):

        if Nums[Index] > Nums[Index - 1]:
            Count += 1
        else:
            Count = 1

        MaxCount = max(MaxCount, Count)

    return MaxCount


print(findLengthOfLCIS([1,3,5,4,7]))