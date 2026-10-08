class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res=set()
        def solve(i):
            if i==len(nums):
                res.add(tuple(nums.copy()))
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                solve(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        solve(0)
        
        return [list(k) for k in res]
