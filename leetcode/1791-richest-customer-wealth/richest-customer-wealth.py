class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_welth=0
     
        for i in range(len(accounts)):
            total=0
            for j in range(len(accounts[i])):
                total+=accounts[i][j]
                
            if total>max_welth:
                max_welth=total
        return max_welth
            