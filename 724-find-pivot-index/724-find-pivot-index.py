class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=0
        total_sum=sum(nums)
        for i in range(len(nums)):
            total_sum-=nums[i]
            if prefix==total_sum:
                return i
            prefix+=nums[i]
        return -1