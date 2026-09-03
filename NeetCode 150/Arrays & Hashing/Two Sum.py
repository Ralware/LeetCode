def twoSum(Nums, Target):
        
    Map = {}
    
    for Index in range(len(Nums)):
        
        Diff = Target - Nums[Index]
        
        if Diff in Map:
            return [Map[Diff],Index]
        
        Map[Nums[Index]] = Index 