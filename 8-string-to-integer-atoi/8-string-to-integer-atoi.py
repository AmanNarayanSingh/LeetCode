
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        s=s.rstrip("-""+")
        if re.match("^[.a-zA-Z]+.*",s):return 0
        i=0
        string=""
        while i<len(s):
            if s[i]=='-' or s[i]=='+':
                string+=s[i]
                i+=1
            elif s[i]>='0' and s[i]<='9':
                string+=s[i]
                i+=1
            else:
                break
        if re.match("^[-+][0-9]+[+-].*",s):
            j=1
            a=""
            a+=string[0]
            while j<len(string):
                a+=string[j]
                j+=1
                if string.index('-')>0 or string[j]=='-' or string[j]=='+':
                    return int(a)
        try:
            
            if int(string)<pow(-2,31):
                return pow(-2,31)
            elif int(string)>pow(2,31)-1:
                return pow(2,31)-1
            return int(string)
        except:
            # print("hi")
            return 0