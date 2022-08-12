class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=0
        total=sum(nums)
        for i in range(len(nums)):
            total-=nums[i]
            if total==prefix:
                return i
            prefix+=nums[i]
        return -1