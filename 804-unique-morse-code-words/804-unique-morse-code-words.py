class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        arr_dict={}
        j=0
        for i in range(97,97+26):
            arr_dict[chr(i)]=morse[j]
            j+=1
        lst=set()
        for i in words:
            string=""
            for j in i:
                string+=arr_dict[j]
            lst.add(string)
        return len(lst)
                