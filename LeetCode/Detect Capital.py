def detectCapitalUse(Word):
    
    if len(Word) <= 1:
        return True
    
    Count = 0     
    
    for Letter in Word:
        if 'A'<= Letter <='Z':
            Count+=1
    
    if Count == 0:
        return True
    
    elif Count == len(Word):
        return True
    
    elif Count == 1 and 'A' <= Word[0] <= 'Z':
            return True
        
    else:
        return False 
    

        