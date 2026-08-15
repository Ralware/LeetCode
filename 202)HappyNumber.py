def isHappy(Num):
       
    def CalculateSum(Num):
        Sum = 0
        for Digit in str(Num):
            Sum += (int(Digit))**2
        return Sum

    CalcSum = CalculateSum(Num)
    Seen = set()

    while CalcSum != 1 and CalcSum not in Seen:
        Seen.add(CalcSum)
        CalcSum = CalculateSum(CalcSum)

    if CalcSum == 1:
        return True
    else:
        return False


print(isHappy(2))