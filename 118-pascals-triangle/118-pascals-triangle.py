class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                temp.append(math.comb(i,j))
            lst.append(temp)
        return lst