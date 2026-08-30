class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result=list()
        T=0
        B=len(matrix)-1
        L=0
        R=len(matrix[0])-1
        while T<=B and L<=R:
            for i in range(L,R+1):
                result.append(matrix[T][i])
            T+=1
            for j in range(T,B+1):
                result.append(matrix[j][R])
            R-=1
            if T<=B:
                for k in range(R,L-1,-1):
                    result.append(matrix[B][k])
                B-=1
            if L<=R:
                for p in range(B,T-1,-1):
                    result.append(matrix[p][L])
                L+=1
        return result