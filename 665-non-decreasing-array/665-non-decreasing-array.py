class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        arr1,arr2=nums[:],nums[:]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                arr1[i],arr2[i+1]=nums[i+1],nums[i]
                break
        return arr1==sorted(arr1) or arr2==sorted(arr2)