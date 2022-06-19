class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr_dict1={}
        for i in range(len(s)):
            if s[i] not in arr_dict1:
                arr_dict1[s[i]]=t[i]
            else:
                if t[i]!=arr_dict1[s[i]]:
                    return False
        arr_dict2={}
        for i in range(len(t)):
            if t[i] not in arr_dict2:
                arr_dict2[t[i]]=s[i]
            else:
                if s[i]!=arr_dict2[t[i]]:
                    return False 
        return True 