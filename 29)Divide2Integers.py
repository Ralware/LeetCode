# Inefficient as hell 

def divide(Dividend, Divisor):
        
        negative = (Dividend < 0) != (Divisor < 0)

        Dividend = abs(Dividend)
        Divisor = abs(Divisor)
        
        count = 0
        
        while Dividend >= Divisor:
            Dividend -= Divisor
            count += 1
        
        return -count if negative else count


print(divide(-2147483648,-1))