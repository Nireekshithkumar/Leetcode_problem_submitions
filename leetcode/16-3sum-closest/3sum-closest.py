class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        cs=float('inf')
         
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                ts=nums[i]+nums[l]+nums[r]
                if abs(cs-target)>abs(ts-target):
                    cs=ts
                if ts>target:
                    r-=1
                elif ts<target:
                    l+=1
                else:
                    return ts
            
        return cs

