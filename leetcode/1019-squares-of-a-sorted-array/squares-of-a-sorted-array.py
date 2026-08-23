class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r=[]
        for i in  nums:
            sq=i*i
            r.append(sq)
        
        r.sort()
        
        return r