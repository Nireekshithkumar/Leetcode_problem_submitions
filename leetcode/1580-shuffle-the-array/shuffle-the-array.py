class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        ans=[]
        for i in range(0,2*n-1,1):
            if n>=len(nums):
                return ans
            else:
                ans.append(nums[i])
                ans.append(nums[n])
                n+=1
        return ans