class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while r>=l:
            mid=(l+r)//2
            if mid*mid>num:
                r=mid-1
            elif mid*mid<num:
                l=mid+1
            else:
                return True
        else:return False