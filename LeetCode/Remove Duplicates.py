def removeDuplicates(Arr):

        NewArr = []
        Count = 0

        for Val in Arr:

            if Val not in NewArr:
                NewArr.append(Val)
                Count+=1
        
        Arr[:] = NewArr

        return Count


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))