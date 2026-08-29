class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        neg=[]
        pos=[]
        res=[]
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        
        i=0
        while i<len(pos) and i<len(neg):
            res.append(pos[i])
            res.append(neg[i])
            i+=1
        return res
            