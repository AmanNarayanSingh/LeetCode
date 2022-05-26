class Solution:
    def hammingWeight(self, n: int) -> int:
        arr=collections.Counter(bin(n).replace("0b",""))
        for k,v in arr.items():
            if k=='1':
                return v
        return 0