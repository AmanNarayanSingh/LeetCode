class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr_dict=collections.Counter(nums)
        for key,values in arr_dict.items():
            if values > len(nums)//2:
                return key