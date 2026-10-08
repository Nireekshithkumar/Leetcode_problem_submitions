class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        def solve(i):
            if i==len(nums):
                res.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                solve(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        solve(0)
        return res
