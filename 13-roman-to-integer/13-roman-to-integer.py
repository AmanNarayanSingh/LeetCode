class Solution:
    def romanToInt(self, s: str) -> int:
        arr_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        integer=0
        for i in range(len(s)-1,-1,-1):
            if i==len(s)-1:
                integer+=arr_dict[s[i]]
            else:
                if arr_dict[s[i]]>=arr_dict[s[i+1]]:
                    integer+=arr_dict[s[i]]
                else:
                    integer-=arr_dict[s[i]]
        return integer 