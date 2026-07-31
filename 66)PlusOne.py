def plusOne(digits):
    StringNum = ""
    for Val in digits:
        StringNum+=str(Val)

    NewNo = int(StringNum)+1

    NumArr = []

    for Val in str(NewNo):
        NumArr.append(int(Val))

    return NumArr


print(plusOne([1,2,3]))