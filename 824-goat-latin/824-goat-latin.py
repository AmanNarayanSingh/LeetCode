class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst=sentence.split()
        # res=[]
        count=1
        res=[]
        # print(lst)
        for i in lst:
            if i[0] in "aeiouAEIOU":
                i=i+"ma"
            elif i[0] not in "aeiouAEIOU":
                temp=list(i)
                a=temp.pop(0)
                temp.append(a)
                i="".join(temp)+"ma"
            i+="a"*count
            # print(i)
            res.append(i)
            count+=1
        return " ".join(res)
            