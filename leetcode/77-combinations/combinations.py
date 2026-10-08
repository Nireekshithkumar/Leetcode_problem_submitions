class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def solve(i,k,sub):
            if k==0:
                res.append(sub.copy())
                return
            if i>n:
                return

            sub.append(i)
            solve(i+1,k-1,sub)
            sub.pop()
            solve(i+1,k,sub)
        solve(1,k,[])
        return res
            