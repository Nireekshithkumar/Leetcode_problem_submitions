class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def recursion(i,total,subseq):
            if total>target:
                return 
            if i==len(candidates):
                return
            
            if total==target:
                res.append(subseq.copy())
        
                return
            subseq.append(candidates[i])
            total+=candidates[i]
            recursion(i,total,subseq)
            e=subseq.pop()
            total-=e
            recursion(i+1,total,subseq)
        recursion(0, 0, [])
        return res