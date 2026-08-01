def strStr(Haystack, Needle):

        for i in range(len(Haystack)):
            if Haystack[i:i+len(Needle)] == Needle :
                return i 
        
        return -1

print(strStr("hello","ll"))