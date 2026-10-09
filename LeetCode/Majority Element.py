def majorityElement(Nums: list[int]) -> int:
    
    Data = {}
    
    for Num in Nums:
        
        if Num not in Data:
            Data[Num] = 1
            
        else:
            Data[Num] += 1
            
    Length = len(Nums)
    
    for Key in Data:
        
        if Data[Key] > Length / 2:
            
            return Key