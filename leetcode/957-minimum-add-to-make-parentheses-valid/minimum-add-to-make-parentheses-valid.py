class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        i=j=0
        for ch in s:
            if ch=='(':
                i+=1
            elif i:
                i-=1
            else:
                j+=1
        return i+j