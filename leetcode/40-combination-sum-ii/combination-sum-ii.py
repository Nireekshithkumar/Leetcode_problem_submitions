class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def solve(i,total,subseq):
            if total==target:
                
                res.append(tuple(sorted(subseq)))
                return
            if i==len(candidates) or total>target:
                return
            subseq.append(candidates[i])
            solve(i+1,total+candidates[i],subseq )
            subseq.pop()
            next_i = i + 1
            while next_i<len(candidates) and candidates[next_i]==candidates[i]:
                next_i+=1
            solve(next_i,total,subseq)
        solve(0, 0, [])
        
       
        return [list(combo) for combo in set(res)]