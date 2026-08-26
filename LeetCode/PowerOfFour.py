import math as Math

def isPowerOfFour(Num):

    if Num < 0 :
        return False
    else:
        if Math.log(Num,4) == int(Math.log(Num,4)):
            return True
        else:
            return False    

print(isPowerOfFour(-64))
        