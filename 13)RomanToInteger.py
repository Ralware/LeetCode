def romanToInt(Roman):
    Num = 0
    for i in range(len(Roman)):
        if Roman[i] == "I":
            Num+=1
        elif Roman[i] == "V":
            Num+=5
        elif Roman[i] == "X":
            Num+=10
        elif Roman[i]== "L":
            Num+=50
        elif Roman[i] == "C":
            Num+=100
        elif Roman[i] == "D":
            Num+=500
        elif Roman[i] == "M":
            Num+=1000
        elif Roman[i] == "I" and Roman[i+1] == "V" :
            Num+=4
        elif Roman[i] == "I" and Roman[i+1] == "X" :
            Num+=9
           
    return Num

print(min(["e","eee"]))

# 1994 

