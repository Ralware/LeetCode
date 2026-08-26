def removeElement(Arr, Element):
        
        NewArr = []
        Count = 0
        
        for Val in Arr:
            if Val == Element :
                Count+=1
            else:
                NewArr.append(Val)

        Arr[:] = NewArr

        return Count,Arr


print(removeElement([0,1,2,2,3,0,4,2],2))

