class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            lst.append(sum(nums[:i+1]))
        return lst