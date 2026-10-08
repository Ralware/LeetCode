def RemoveElement(Arr):
    
    Dict = {}
    
    for Element in Arr:
        if not Element in Dict:
            Dict[Element] = 1
        else:
            Dict[Element] += 1
        
    FinalArr = []
            
    for Key in Dict:
        
        if Dict[Key] <= 2:
            for _ in range(Dict[Key]):
                FinalArr.append(Key)  
        else:
            for _ in range(2):
                FinalArr.append(Key)                          
                
    Arr[:] = FinalArr

print(RemoveElement([1,1,2,2,2,3]))             
