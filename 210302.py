import numpy as np
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums = sorted(nums)
        complete_set = set(np.arange(1,len(nums)+1))
        dup = None
        nums_set = set()
        for ele in nums:
            if ele not in nums_set:
                nums_set.add(ele)
            elif dup is None:
                dup = ele
        # print(complete_set)
        # print(nums_set)
        miss = list(complete_set - nums_set)[0]
        
        return [dup,miss]