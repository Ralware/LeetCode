def findMaxConsecutiveOnes(NumsArr):
        
        Count = 0
        CountArr = []

        for i in range(len(NumsArr)):

            if NumsArr[i]:
                Count += 1
            else:
                CountArr.append(Count)
                Count = 0

        if Count:
            CountArr.append(Count)

        return max(CountArr)
                


print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))

