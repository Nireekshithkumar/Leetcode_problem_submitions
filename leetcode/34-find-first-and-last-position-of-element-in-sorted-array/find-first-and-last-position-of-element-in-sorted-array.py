class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower=self.lowerBound(nums,target)
        if lower==-1 or lower==len(nums) or nums[lower]!=target:
            return [-1, -1]
        else:
            Upper=self.UpperBound(nums,target)
        return [lower,Upper]
        
    
    def lowerBound(self,nums,target):
        n=len(nums)
        LB=-1
        L,H=0,n-1
        while L<=H:
            mid=(L+H)//2
            if nums[mid]>=target:
                LB=mid
                H=mid-1
            else:
                L=mid+1
        
        return LB
    def UpperBound(self,nums,target):
        n=len(nums)
        UB=n
        L,H=0,n-1
        while L<=H:
            mid=(L+H)//2
            if nums[mid]>target:
                UB=mid
                H=mid-1
            else:
                L=mid+1
        
        return UB-1

        
        