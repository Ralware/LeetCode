
def addDigits(Num):
    NumDigits = []

    for Digit in str(Num):
        NumDigits.append(int(Digit))
    
    # [3,8]

    Sum = 0

    for Val in NumDigits:
        Sum+=Val

    if len(str(Sum)) == 1:
        return Sum
    else:
        return addDigits(Sum)

        
print(addDigits(823))


        
        