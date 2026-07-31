def moveZeroes(Nums):

    FinalNum = []
    NonZeros = []

    for Index in range(len(Nums)):
        if  Nums[Index] == 0:
            FinalNum = FinalNum + [0]
        else:
            NonZeros  = NonZeros + [Nums[Index]] 

    return NonZeros+FinalNum
    

print(moveZeroes([0,1,0,3,12]))
        