def myAtoi(NumStr):

        Nums = "1234567890"
        NumArr = ""
        
        for i in range(len(NumStr)):

                if NumStr[i] == " ":
                        continue
                
                if NumStr[i] not in Nums:
                        break
            
                if NumStr[i] in Nums:
                        NumArr+=NumStr[i]

            

        return NumArr

print(myAtoi("   -042"))