class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        n=len(nums)
        i=0
        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[j],nums[i]=nums[i],nums[j]
                
           
            j+=1
        
        return i+1