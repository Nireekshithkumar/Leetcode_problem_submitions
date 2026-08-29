class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x=0
        max=0
        for i in nums:
            if i==1:
                x+=1
                
            else:
                x=0
            if max<x:
                max=x
        return max
        