class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        max_val=float('-inf')
        for i in range(0,len(nums)):  
            total+=nums[i]
            max_val=max(max_val,total)
            if total<0:
                total=0
        return max_val