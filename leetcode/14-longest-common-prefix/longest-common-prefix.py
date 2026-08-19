class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmn=""
        v=sorted(strs)
       
        first=v[0]
        last=v[len(strs)-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return cmn
            cmn+=first[i]
        return cmn
        
            
        