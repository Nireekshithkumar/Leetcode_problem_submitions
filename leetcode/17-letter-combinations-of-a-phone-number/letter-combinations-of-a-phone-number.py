class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pair = {
             
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
            
        }
        res=[]
        def solve(i,sub):
            

            if i==len(digits) :
                res.append(sub)
                return

            for j in pair[digits[i]]:
                solve(i+1,sub+j)
        solve(0,'')
        return res

