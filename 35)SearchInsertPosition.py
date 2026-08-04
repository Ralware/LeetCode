def searchInsert(Nums, Target):
    
    Low = 0
    High = len(Nums)-1
    while High >= Low:
        Mid = ( Low + High ) // 2
        if Target > Nums[Mid]:
            Low = Mid + 1
        elif Target < Nums[Mid]:
            High = Mid - 1
        else:
            return Mid
    
    return Low