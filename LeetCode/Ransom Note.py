class Solution:
    def canConstruct(self, RansomNote: str, Magazine: str) -> bool:
        Data_1 = {}
        Data_2 = {}

        for Letter in RansomNote:
            if Letter not in Data_1:
                Data_1[Letter] = 1
            else:
                Data_1[Letter] += 1

        for Letter in Magazine:
            if Letter not in Data_2:
                Data_2[Letter] = 1
            else:
                Data_2[Letter] += 1

        for Key in Data_1:
            if Key not in Data_2:
                return False      #Case Where Some RansomNote Key Isn't In Magazine   

            if Data_1[Key] > Data_2[Key]:
                return False

        return True