class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        low,high,digit,special=0,0,0,0
        length=len(password)
        password+="~"
        for i in range(len(password)-1):
            if ord(password[i])>=65 and ord(password[i])<=90:
                low=1
            elif ord(password[i])>=97 and ord(password[i])<=122:
                high=1
            elif password[i] in "!@#$%^&*()-+":
                special=1
            elif ord(password[i])>=48 and ord(password[i])<=57:
                digit=1
            if password[i]==password[i+1]:
                return False 
        # print(low,high,digit,special)
        if low and high and digit and special and length>=8:
            return True 
             