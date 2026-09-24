class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp=n&n-1
        if n==0:
            return False
        
        return True if temp==0 else False

        
        