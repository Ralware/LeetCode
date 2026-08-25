def myPow(Base: float, Power: int) -> float:

        Final = 1.0

        for _ in range(abs(Power)):
            Final *= Base
        
        if Power < 0 :
            return (1.0/Final)
        else:
            return Final 

print(myPow(2,-5))
