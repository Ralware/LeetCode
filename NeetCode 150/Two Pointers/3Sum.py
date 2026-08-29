# Not Quite Right !

def threeSum(Nums):

    Solutions = []
    
    for Index in range(len(Nums)):
        
        Low = 0
        
        High = len(Nums) - 1
        
        print(f"Trial {Index+1}")
        
        while Low < Index and High > Index:
            
            Sum = Nums[Index] + Nums[Low] + Nums[High]
            print(Sum)
            
            if Sum < 0 :
                Low += 1
                
            elif Sum > 0 :
                High += 1
                
            else:
                Solutions.append([Nums[Index],Nums[Low],Nums[High]])

    return Solutions

