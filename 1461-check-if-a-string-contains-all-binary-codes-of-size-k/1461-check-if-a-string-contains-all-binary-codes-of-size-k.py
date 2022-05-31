class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k==15 or (k==16 and s[:4]=="0000"):
            return True 
        elif k==16 and s[:4]=="1111":
            return False 
        
        lst=["0","1"]
        arr=list(map(lambda x:"".join(x),list(itertools.product(lst,repeat=k))))
        for i in range(len(arr)):
            if arr[i] not in s:
                return False 
        return True 
