def isPalindrome(x):
        
        if x < 0 :
            return False
        
        return True if int(str(x)[::-1]) == x else False

print(isPalindrome(-100))