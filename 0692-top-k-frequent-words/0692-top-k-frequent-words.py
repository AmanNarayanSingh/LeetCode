class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res_dict=dict(sorted(collections.Counter(words).items()))
        res_dict=dict(sorted(res_dict.items(),key=operator.itemgetter(1),reverse=True))
        # for key,val in res_dict.items():
        #     print(key,val)
        return list(res_dict.keys())[:k]