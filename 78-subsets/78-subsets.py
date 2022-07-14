class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst=[[]]
        # lst.add([])
        for i in range(1,len(nums)+1):
            a=list(itertools.combinations(nums,i))
            for j in a:
                lst.append(j)
        return lst