class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp=n

        while temp>0:
            if temp==1:
                return True
            elif not temp%2==0:
                return False
            temp=temp//2
        return False

        
        