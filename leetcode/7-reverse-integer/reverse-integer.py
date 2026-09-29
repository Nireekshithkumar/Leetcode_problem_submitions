class Solution:
    def reverse(self, x: int) -> int:
        
        temp=x
        res=0
        if temp<0:
            temp*=-1
        while temp!=0:
            last=temp%10
            res=res*10+last
            temp//=10
        
        if res in range(-2**31 ,2**31):
            return res if x>0 else  res*-1
        else:
            return 0