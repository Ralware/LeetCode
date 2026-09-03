# Input: Nums = [1,1,3,4], Target = 2
# Output: [1,2]

def twoSum(Nums,Target):
    
    Data = {}
    
    for Index in range(len(Nums)):
        
        if (Target-Nums[Index]) in Data:
            return [Data[Target-Nums[Index]]+1,Index+1]
        
        Data[Nums[Index]] = Index
    
    return []

