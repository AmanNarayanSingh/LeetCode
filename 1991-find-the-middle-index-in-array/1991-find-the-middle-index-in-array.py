class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix,total=0,sum(nums)
        for i in range(len(nums)):
            total-=nums[i]
            if prefix==total:
                return i
            prefix+=nums[i]
        return -1