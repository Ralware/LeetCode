def longestCommonPrefix(WordsArr):
        
        SmallestWord = min(WordsArr,key=len)

        if len(WordsArr) == 1:
            return WordsArr[0]
        
        elif SmallestWord == "":
            return ""

        Slices = []

        FinalSlice = ""

        for Index in range(len(SmallestWord)):
            Slice = SmallestWord[:Index+1]

            for Word in WordsArr:
                if Slice == Word[:Index+1]:
                    Valid = True
                else:
                     Valid = False
                     break
            if Valid:
                 FinalSlice = Slice
                  
                      
        return FinalSlice 
                          
print(longestCommonPrefix(["flower","flow","flight"]))