class Solution:
    def hammingWeight(self, n: int) -> int:
        temp=n
        res=0
        while temp!=0:
            if temp%2!=0:
                res+=1
            temp=temp//2
        return res
        