class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
       
        myset=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)): 
                res=list()
                for k in range(j+1,len(nums)):
                    
                    fourth= target-(nums[i]+nums[j]+nums[k])
                    if fourth in res:
                        temp=[nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        myset.add(tuple(temp))
                    res.append(nums[k])
        return [list(ele) for ele in myset]