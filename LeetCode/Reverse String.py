def reverseString(s):
        s[:] = list("".join(s)[::-1])
        return s

print(reverseString(["h","e","l","l","o"]))