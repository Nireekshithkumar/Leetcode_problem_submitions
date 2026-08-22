class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min=nums[0]
        for i in nums[1:]:
            if abs(i)<abs(min):
                min=i
            elif abs(i)==abs(min) and i>0:
                min=i
        return min

            
        