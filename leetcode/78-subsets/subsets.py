class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        sub_len=(1<<n)
        res=[]
        for i in range(0,sub_len):
            let=[]
            for j in range(n):
                if i & (1<<j)!=0:
                    let.append(nums[j])
            res.append(let)
        
        return res