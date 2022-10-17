class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res=list(set(list(sentence)))
        return True if len(res)==26 else False 