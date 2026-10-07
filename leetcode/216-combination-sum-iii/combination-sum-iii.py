class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        res=[]
        def solve(i,total,sub):
           
            if total==n and len(sub)==k:
                res.append(sub.copy())
                return
            if total>n or len(sub)>k:
               return
            for j in range(i,10):
               
                sub.append(j)
                solve(j+1,total+j,sub)
                sub.pop()
                

        solve(1,0,[])
        return res