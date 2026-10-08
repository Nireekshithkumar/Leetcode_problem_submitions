class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=[]
        board=["."*n for _ in range(n)]
        self.solve(0,board,ans,n)
        return len(ans)
    def solve(self,col,board,ans,n):
        if col==n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                self.solve(col+1,board,ans,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
    
    def isSafe(self,row,col,board,n):
        dupcol=col
        duprow=row

        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        col=dupcol
        row=duprow

        while col>=0:
            if board[row][col]=='Q':
                return False
            col-=1
        col=dupcol
        row=duprow

        while row<n and col >=0:
            if board[row][col]=='Q':
                return False
            col-=1
            row+=1
        return True