def isUgly(Num: int) -> bool:
        if Num == 1:
            return True
        elif Num <= 0:
            return False
    
        while Num > 1:
            if Num % 2 == 0:
                Num = Num//2
            elif Num % 3 == 0:
                Num = Num//3
            elif Num % 5 == 0:
                Num = Num//5
            else:
                return False
        
        return True